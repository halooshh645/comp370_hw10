provider = google
model = gemini-3.5-flash-lite
1. What labels did it preform well on?

The annotator performed particularly well on CFS, CESB, and SWB, achieving both perfect precision and recall for these categories. However, these categories had relatively few posts, so these results should be interpreted cautiously.

AAC and SLA also had high precision, meaning that when Gemini predicted these categories, it was usually correct. However, their recall was lower, indicating that Gemini missed some posts that actually belonged to these categories.

HT had perfect recall but relatively low precision (0.50), meaning that it identified all actual HT posts but also incorrectly assigned another post to this category.

PSI cannot be evaluated, because there were no actual or predicted posts in that category.

2. What labels did it fail on?

Gemini performed less well on APP and HT, which had precision scores of 0.58 and 0.50, respectively. This means that a relatively large proportion of posts predicted as belonging to these categories were incorrectly classified. For APP, Gemini correctly classified only 7 of the 12 posts it predicted as APP. For HT, it correctly classified only 1 of the 2 posts it predicted as HT. However, the HT result should be interpreted cautiously because there were very few posts in this category.

3. Where was it confused?
Gemini was mostly confused between AAC and APP. It incorrectly classified four AAC posts as APP, including posts about individual courses such as "ECON 480: Research Project 1 Guidance" and "BTM 480." This suggests that Gemini sometimes had difficulty distinguishing between questions about coursework and questions about academic programs.

There were also a few other errors. Gemini classified one APP post about graduates moving to Ontario as HT, possibly because it interpreted moving as a housing-related topic. It also incorrectly classified one SLA post about a student survey as APP.
