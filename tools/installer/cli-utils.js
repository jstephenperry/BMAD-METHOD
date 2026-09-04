const prompts = require('./prompts');

const CLIUtils = {
  /**
   * Display the Continuous Agile logo and version using @clack intro + box
   */
  async displayLogo() {
    const color = await prompts.getColor();
    const termWidth = process.stdout.columns || 80;

    // A "CA" monogram. Deliberately compact: it fits every terminal width, so
    // there is no wide/narrow variant to keep in sync.
    const monogram = [
      ' ██████╗ █████╗ ',
      '██╔════╝██╔══██╗',
      '██║     ███████║',
      '██║     ██╔══██║',
      '╚██████╗██║  ██║',
      ' ╚═════╝╚═╝  ╚═╝',
    ];

    const logo = monogram.map((line) => color.blue(line)).join('\n');
    // The monogram carries the initials, so the line below spells the name out.
    const wordmark = color.white(termWidth >= 95 ? '    C O N T I N U O U S   A G I L E' : '    Continuous Agile');
    const tagline = color.dim('    Full-lifecycle agentic development');

    await prompts.box(`${logo}\n${wordmark}\n${tagline}`, '', {
      contentAlign: 'center',
      rounded: true,
      formatBorder: color.blue,
    });
  },

  /**
   * Display module configuration header
   * @param {string} moduleName - Module name (fallback if no custom header)
   * @param {string} header - Custom header from module.yaml
   * @param {string} subheader - Custom subheader from module.yaml
   */
  async displayModuleConfigHeader(moduleName, header = null, subheader = null) {
    const title = header || `Configuring ${moduleName.toUpperCase()} Module`;
    await prompts.note(subheader || '', title);
  },
};

module.exports = { CLIUtils };
