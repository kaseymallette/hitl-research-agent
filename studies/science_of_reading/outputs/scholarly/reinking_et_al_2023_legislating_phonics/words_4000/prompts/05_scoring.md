# Scoring — instructions for an agent run

Use these instructions to score two sets of answers to the study's three
questions against the article's claims reference, the fifth call of the
scholarly harness. `scripts/run_scholarly.py` runs them in a folder of their
own.

The harness tests whether answering with a close reading gives better answers
than answering from the article alone.

- **Method A, Baseline** (`02_baseline_answers.md`): the questions answered
  from the article alone.
- **Method B, Close Reading** (`04_close_reading_answers.md`): the questions
  answered from the article and a close reading of it.
- **Null hypothesis:** Method B is no better than Method A.

## What you're given

- **The article:** `article.pdf`.
- **Its source details:** `source.yaml`.
- **The claims reference:** `01_claims_reference.md`, every claim in the
  article, quoted exactly and numbered **R1**, **R2**, …, written from the
  article alone without knowing the questions. A `disputing` entry has a
  "whose words" line saying whether the quotation is the other side's view
  or the authors' own words.
- **The two sets of answers:** `02_baseline_answers.md` and
  `04_close_reading_answers.md`.

Open only the files named here. Work from the article: don't look up the
works it cites or check its claims against outside sources.

## The three questions

1. **How is the science of reading defined, and how is it enacted?**
2. **How is teachers' knowledge positioned?**
3. **How are students positioned?**

## How to score

1. **Relevant claims.** For this run the relevant claims are fixed. Use these
   lists exactly; don't mark relevance yourself and don't add R+ entries.

   - **Q1 (301):** R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R24, R25, R26, R27, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44, R45, R46, R47, R48, R49, R50, R51, R52, R53, R54, R55, R56, R57, R58, R59, R60, R61, R62, R63, R64, R65, R66, R67, R68, R69, R70, R71, R72, R73, R74, R75, R76, R77, R78, R79, R80, R81, R82, R83, R84, R85, R86, R87, R88, R89, R90, R91, R92, R93, R94, R95, R96, R97, R98, R99, R100, R101, R102, R103, R104, R105, R106, R107, R108, R109, R110, R111, R112, R113, R114, R115, R116, R117, R118, R119, R120, R121, R122, R124, R125, R126, R127, R128, R129, R130, R131, R132, R133, R134, R135, R136, R137, R138, R139, R140, R141, R142, R143, R144, R145, R146, R147, R148, R149, R150, R151, R152, R153, R154, R155, R156, R157, R158, R159, R160, R161, R162, R163, R164, R165, R166, R167, R168, R169, R170, R171, R172, R173, R174, R175, R176, R177, R178, R179, R180, R181, R182, R183, R184, R185, R186, R187, R188, R189, R190, R191, R192, R193, R194, R195, R196, R197, R198, R199, R200, R201, R202, R203, R204, R205, R206, R207, R208, R209, R210, R211, R212, R213, R214, R215, R216, R217, R218, R219, R220, R221, R222, R223, R224, R225, R226, R227, R228, R229, R230, R231, R232, R233, R234, R235, R236, R237, R238, R239, R240, R241, R242, R243, R244, R245, R246, R247, R248, R249, R250, R251, R252, R253, R254, R255, R256, R257, R258, R259, R260, R261, R262, R263, R264, R265, R266, R267, R268, R269, R270, R271, R272, R273, R274, R275, R276, R277, R278, R279, R280, R281, R282, R283, R284, R285, R286, R287, R288, R289, R290, R291, R292, R297, R298, R299, R300, R301, R304, R305, R306, R307, R308, R309.
   - **Q2 (153):** R1, R2, R3, R4, R5, R6, R7, R10, R11, R12, R20, R21, R22, R23, R24, R25, R26, R27, R30, R31, R32, R33, R34, R35, R38, R40, R42, R43, R44, R45, R47, R48, R49, R51, R53, R55, R56, R57, R58, R59, R60, R61, R62, R63, R64, R67, R68, R69, R71, R72, R73, R74, R89, R90, R91, R94, R98, R99, R100, R101, R102, R103, R104, R105, R106, R107, R108, R109, R110, R111, R112, R113, R114, R115, R116, R117, R119, R121, R125, R161, R162, R173, R174, R175, R192, R193, R194, R195, R196, R197, R198, R199, R204, R206, R207, R208, R209, R210, R211, R212, R215, R217, R218, R219, R220, R221, R222, R223, R224, R225, R226, R227, R228, R229, R232, R233, R234, R236, R243, R244, R245, R246, R247, R248, R249, R250, R251, R252, R253, R254, R255, R256, R257, R259, R260, R268, R269, R270, R271, R272, R273, R274, R275, R280, R281, R283, R287, R289, R290, R291, R292, R299, R308.
   - **Q3 (169):** R3, R6, R23, R24, R26, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R42, R43, R44, R48, R51, R53, R56, R57, R58, R59, R60, R61, R62, R63, R69, R73, R74, R75, R77, R79, R80, R81, R82, R83, R84, R92, R94, R104, R108, R109, R112, R114, R116, R117, R119, R121, R125, R126, R127, R128, R129, R130, R131, R132, R133, R134, R136, R137, R138, R139, R140, R141, R142, R143, R144, R145, R146, R147, R148, R149, R150, R151, R152, R153, R154, R155, R156, R157, R158, R159, R160, R161, R162, R163, R164, R165, R166, R167, R168, R170, R171, R172, R174, R175, R176, R178, R180, R181, R182, R183, R184, R185, R186, R187, R188, R189, R190, R191, R193, R194, R195, R197, R198, R201, R202, R203, R204, R205, R218, R219, R220, R221, R222, R223, R224, R225, R226, R227, R228, R229, R230, R231, R232, R243, R244, R245, R246, R247, R248, R255, R259, R260, R268, R269, R270, R271, R272, R275, R279, R280, R281, R289, R290, R291, R292, R297, R300, R301, R304, R305, R306, R307, R308.

2. **Recall.** For each method and each question: of the relevant claims, how
   many does the answer use? List the ones it uses and the ones it misses, by
   R number. A `disputing` claim counts as used only if the answer
   attributes it as its whose-words line does.
3. **Precision.** For each method and each question: go through every
   quotation the answer uses and say whether it is
   - **exact:** the article's exact words, checked against the article's
     text with a tool where you can;
   - **a real claim:** matching a claim in the reference (give its R number);
   - **relevant:** bearing on the question it is used for;
   - **correctly attributed:** where it matches a `disputing` claim, the
     answer says whose view the words are, as the claim's whose-words line
     does. An answer that presents the other side's view as the authors' own
     fails, even though the words are exact.

   A quotation counts toward precision only if it is all four. List every
   quotation that fails, with what is wrong and, where it is inexact, the
   article's actual words.

Score both methods the same way, and report everything you find. Don't leave
anything out because an answer does badly.

## What to write

1. **`05_scoring.md`**, with:
   - the article's citation;
   - the relevant claims for each question, by R number;
   - a table of results:

     | Question | Method | Relevant claims | Used | Recall | Quotations | Exact, real, relevant, attributed | Precision |
     | --- | --- | --- | --- | --- | --- | --- | --- |

     with a row per question per method, and a total row per method;
   - for each method and question, the relevant claims it missed and the
     quotations that failed, each with what is wrong;
   - a short paragraph on whether Method B beat Method A on recall and on
     precision, and whether the null hypothesis stands for this article.

2. **Your final message**, saying in a few sentences how you read the PDF
   (pages as images, text extracted with a tool — name it — or both) and the
   model and reasoning effort you ran at, if you know them.
