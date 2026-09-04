---
title: "Cách tìm câu trả lời về Continuous Agile"
description: Sử dụng LLM để tự nhanh chóng trả lời các câu hỏi về Continuous Agile
sidebar:
        order: 4
---

Hãy dùng trợ giúp tích hợp sẵn của Continuous Agile, tài liệu nguồn, hoặc cộng đồng để tìm câu trả lời, theo thứ tự từ nhanh nhất đến đầy đủ nhất.

## 1. Hỏi BMad-Help

Cách nhanh nhất để có câu trả lời. Skill `bmad-help` có sẵn ngay trong phiên AI của bạn và xử lý được hơn 80% câu hỏi. Nó sẽ kiểm tra dự án, nhìn xem bạn đã hoàn thành đến đâu và cho bạn biết nên làm gì tiếp theo.

```text
bmad-help Tôi có ý tưởng SaaS và đã biết tất cả tính năng. Tôi nên bắt đầu từ đâu?
bmad-help Tôi có những lựa chọn nào cho thiết kế UX?
bmad-help Tôi đang bị mắc ở workflow PRD
```

:::tip
Bạn cũng có thể dùng `/bmad-help` hoặc `$bmad-help` tùy nền tảng, nhưng chỉ `bmad-help` là cách nên hoạt động mọi nơi.
:::

## 2. Đi sâu hơn với mã nguồn

BMad-Help dựa trên cấu hình bạn đã cài đặt. Nếu bạn cần tìm hiểu nội bộ, lịch sử, hay kiến trúc của Continuous Agile, hoặc đang nghiên cứu nó trước khi cài, hãy để AI đọc trực tiếp mã nguồn.

Hãy clone hoặc mở [repo Continuous Agile](https://github.com/jstephenperry/continuous-agile) rồi hỏi AI của bạn về nó. Bất kỳ công cụ nào có hỗ trợ agent như Claude Code, Cursor, Windsurf... đều có thể đọc mã nguồn và trả lời trực tiếp.

:::note[Ví dụ]
**Q:** "Hãy chỉ tôi cách nhanh nhất để xây dựng một thứ gì đó bằng Continuous Agile"

**A:** Chạy `bmad-build`. Đưa vào ý định trực tiếp, issue, spec hoặc story đã lập kế hoạch; workflow dùng ngữ cảnh sẵn có và chọn độ sâu làm rõ, lập kế hoạch, triển khai và review cần thiết.
:::

**Mẹo để có câu trả lời tốt hơn:**

- **Hãy hỏi thật cụ thể** - "Bước 3 trong workflow PRD làm gì?" sẽ tốt hơn "PRD hoạt động ra sao?"
- **Kiểm tra lại những câu trả lời nghe lạ** - LLM đôi khi vẫn sai. Hãy kiểm tra file nguồn hoặc mở issue trên GitHub.

### Không dùng agent? Dùng file tài liệu

Nếu AI của bạn không đọc được file cục bộ như ChatGPT hoặc Claude.ai, hãy chạy `npm run docs:build` trong repo rồi nạp file `llms-full.txt` vừa được sinh ra vào phiên làm việc. Đây là bản chụp toàn bộ tài liệu Continuous Agile trong một file duy nhất.

## 3. Hỏi người thật

Nếu cả BMad-Help lẫn mã nguồn vẫn chưa trả lời được câu hỏi của bạn, lúc này bạn đã có một câu hỏi rõ hơn nhiều để đem đi hỏi cộng đồng.

**GitHub Issues:** [github.com/jstephenperry/continuous-agile/issues](https://github.com/jstephenperry/continuous-agile/issues) — câu hỏi, báo lỗi, ý tưởng và đề xuất tính năng

*Chính bạn,*
        *đang mắc kẹt*
             *trong hàng đợi -*
                      *đợi*
                              *ai?*

*Mã nguồn*
        *nằm ngay đó,*
                *rõ như ban ngày!*

*Hãy trỏ*
        *cho máy của bạn.*
                    *Thả nó đi.*

*Nó đọc.*
        *Nó nói.*
                *Cứ hỏi -*

*Sao phải chờ*
        *đến ngày mai*
                *khi bạn đã có*
                        *ngày hôm nay?*

*- Claude*
