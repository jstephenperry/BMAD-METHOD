const path = require('node:path');
const fs = require('../fs-native');
const { Manifest } = require('./manifest');

/**
 * Immutable snapshot of an existing BMAD installation.
 * Pure query object — no filesystem operations after construction.
 */
class ExistingInstall {
  #version;

  constructor({ installed, version, hasCore, modules, ides }) {
    this.installed = installed;
    this.#version = version;
    this.hasCore = hasCore;
    this.modules = Object.freeze(modules.map((m) => Object.freeze({ ...m })));
    this.moduleIds = Object.freeze(this.modules.map((m) => m.id));
    this.ides = Object.freeze([...ides]);
    Object.freeze(this);
  }

  get version() {
    if (!this.installed) {
      throw new Error('version is not available when nothing is installed');
    }
    return this.#version;
  }

  static empty() {
    return new ExistingInstall({
      installed: false,
      version: null,
      hasCore: false,
      modules: [],
      ides: [],
    });
  }

  /**
   * Scan a bmad directory and return an immutable snapshot of what's installed.
   * @param {string} bmadDir - Path to bmad directory
   * @returns {Promise<ExistingInstall>}
   */
  static async detect(bmadDir) {
    if (!(await fs.pathExists(bmadDir))) {
      return ExistingInstall.empty();
    }

    let version = null;
    let hasCore = false;
    const modules = [];
    let ides = [];

    const manifest = new Manifest();
    const manifestData = await manifest.read(bmadDir);
    if (manifestData) {
      version = manifestData.version;
      if (manifestData.ides) {
        ides = manifestData.ides.filter((ide) => ide && typeof ide === 'string');
      }
    }

    const corePath = path.join(bmadDir, 'core');
    if (await fs.pathExists(corePath)) {
      hasCore = true;
    }

    if (manifestData && manifestData.modules && manifestData.modules.length > 0) {
      for (const moduleId of manifestData.modules) {
        modules.push({
          id: moduleId,
          path: path.join(bmadDir, moduleId),
          version: 'unknown',
        });
      }
    }

    const installed = hasCore || modules.length > 0 || !!manifestData;

    if (!installed) {
      return ExistingInstall.empty();
    }

    return new ExistingInstall({ installed, version, hasCore, modules, ides });
  }
}

module.exports = { ExistingInstall };
