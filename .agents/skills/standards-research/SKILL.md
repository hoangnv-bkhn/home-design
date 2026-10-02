---
name: standards-research
description: Research and verify Vietnamese building codes, planning regulations (QCVN/TCVN), and cultural feng shui guidance with rigorous citations. Use when investigating setbacks, stair standards, boundary opening rights, daylight/ventilation, or altar placement.
---

# Vietnamese Building Standards & Cultural Research

Use this skill when researching statutory building codes, construction planning regulations, architectural standards, or feng shui guidance for this residential house project in Soc Son / Noi Bai, Hanoi.

In Antigravity, you can invoke this skill as `standards-research` or via the slash command `/standards-research`.

## Core Standards Reference

When investigating technical questions, consult the following authoritative Vietnamese regulations:

| Code / Standard | Full Vietnamese Title | Key Subject Areas Relevant to Project |
| :--- | :--- | :--- |
| **QCVN 01:2021/BXD** | Quy chuẩn kỹ thuật quốc gia về Quy hoạch xây dựng | Mật độ xây dựng (building density), khoảng lùi công trình (statutory setbacks), độ vươn ban công / ô văng (balcony projections), chiều cao tầng |
| **QCVN 06:2022/BXD** (với **Sửa đổi 1:2023**) | Quy chuẩn kỹ thuật quốc gia về An toàn cháy cho nhà và công trình | Khoảng cách an toàn phòng cháy chữa cháy, lối thoát nạn, vật liệu ngăn cháy |
| **TCVN 9411:2012** | Nhà ở liên kế — Tiêu chuẩn thiết kế | Kích thước tối thiểu các phòng; chiều cao thông thủy; kích thước thang (chiều rộng vế thang, bậc thang: chiều rộng mặt bậc $\ge 250\text{ mm}$, chiều cao bậc $\le 180\text{ mm}$, số bậc liên tục $\le 18$); giếng trời và thông gió chiếu sáng tự nhiên; quy định mở cửa sổ giáp ranh |
| **Bộ luật Dân sự 2015** (Điều 178) | Quyền về trổ cửa nhìn sang bất động sản liền kề | Giới hạn mở cửa sổ, lỗ thông hơi tiếp giáp trực tiếp ranh giới đất của chủ sở hữu liền kề |
| **Luật Xây dựng 2014** (sửa đổi 2020) | Luật Xây dựng | Điều kiện cấp giấy phép xây dựng nhà ở riêng lẻ, quản lý chỉ giới đường đỏ và chỉ giới xây dựng |

## Evidential Invariants (from `AGENTS.md`)

1. **No calculations from snippets**: Never base compliance claims or dimensional decisions on unverified forum posts, casual blog articles, or secondary snippets.
2. **Mandatory citation format**:
   - **Document code & edition**: e.g., `TCVN 9411:2012`, `QCVN 01:2021/BXD`.
   - **Specific clause / article / table**: e.g., `Điều 6.3.2.1`, `Bảng 2.8`.
   - **Source & access date**: e.g., Thư viện Pháp luật / Cổng thông tin điện tử Bộ Xây dựng (vbpl.vn, thuvienphapluat.vn), accessed `YYYY-MM-DD`.
   - **Applicability & limitations**: Clearly distinguish mandatory regulations (QCVN) from recommended design standards (TCVN), and rural/peri-urban planning status for this specific site.
3. **Feng Shui as cultural guidance**:
   - Treat feng shui strictly as cultural guidance and the family's chosen interpretation (1993 Quy Dau, Tay Tu Menh, SE road arrival, altar SE with solid backing wall).
   - Record source quality and uncertainty. Never introduce new family constraints unprompted or claim guaranteed health/wealth outcomes.

## Antigravity Research Tools Workflow

When executing this skill in Antigravity:
1. Use `search_web` to locate official legal documents:
   - Query pattern: `site:vbpl.vn "QCVN 01:2021/BXD" "khoảng lùi"` or `site:thuvienphapluat.vn "TCVN 9411:2012" "cầu thang"`.
2. Use `read_url_content` to retrieve the authentic text directly from official legal databases (vbpl.vn, moc.gov.vn, thuvienphapluat.vn).
3. If deep investigation is required while preserving main task context, launch a `research` subagent via `invoke_subagent`.
4. Synthesize findings into the project's durable documentation:
   - Add new confirmed requirements or constraints to `docs/brief.md` or `docs/preferences-and-feng-shui.md`.
   - Record resolved questions in `docs/decisions.md`.
   - Update unresolved tracking items in `docs/open-issues.md` (e.g. issues S02, L06, L10, E01).
