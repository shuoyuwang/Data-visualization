# Step
1. Crawl data: through the request method to get the target website URL caseList and converted into json data, stored in excel. 
<img width="388" alt="image" src="https://github.com/shuoyuwang/Data-visualization/assets/59498813/848a8bbf-a668-442d-83f3-5543aeb20dc3">

2. Use the scatter function of the pyecharts library to draw a scatterplot based on the existing diagnosis volume in Beijing, Shanghai, Guangdong, and Tianjin, for example.
<img width="369" alt="image" src="https://github.com/shuoyuwang/Data-visualization/assets/59498813/89b4688b-072a-428f-aef9-84ecb5a70cfe">

3. Use the line function of pyecharts library to draw a line graph based on the existing diagnosis in Beijing, Shanghai, Guangdong and Tianjin for example.
<img width="416" alt="image" src="https://github.com/shuoyuwang/Data-visualization/assets/59498813/97cd0b95-19ed-4212-8527-2ec8ea81e8b7">

4. Use the bar function of the pyecharts library to draw a horizontal bar chart based on the cumulative number of confirmed cases in Beijing, Shanghai, Guangdong and Tianjin, for example.
<img width="415" alt="image" src="https://github.com/shuoyuwang/Data-visualization/assets/59498813/eebeb49b-b14c-4ccb-84fa-996fffa17fca">

5. Use the bar function of the pyecharts library to draw a positive and negative bar chart based on the existing confirmed diagnoses and the incremental number of existing confirmed diagnoses in Beijing, Shanghai, Guangdong, and Tianjin, for example.

<img width="416" alt="image" src="https://github.com/shuoyuwang/Data-visualization/assets/59498813/a1985d9a-40eb-40e7-8493-17c45a07be89">

6. Use the bar function of the pyecharts library to draw a vertical bar chart based on the cumulative number of confirmed diagnoses in Asia, Europe, Africa, Oceania, North America, and South America, for example.

<img width="416" alt="image" src="https://github.com/shuoyuwang/Data-visualization/assets/59498813/9695814b-4ec8-4325-90a6-f4400dad62f2">

7. Use the plotly library figure function to draw a pie chart based on the cumulative number of confirmed diagnoses in Beijing, Shanghai, Guangdong, and Tianjin, for example, and highlight the part of the pie chart for Beijing.

<img width="416" alt="image" src="https://github.com/shuoyuwang/Data-visualization/assets/59498813/0390449a-b5d5-45d6-ac31-11808e91b3bc">

8. Use plotly library figure function to plot Asia, Europe, Africa, Oceania, North America, South America, for example, based on the cumulative number of confirmed cases to draw a pie chart, highlighting the part of the pie chart in Asia.

<img width="416" alt="image" src="https://github.com/shuoyuwang/Data-visualization/assets/59498813/90b10ded-cefc-4cfc-84d9-9a5a933aa791">

9. Use pyecharts library pie function to Beijing, Shanghai, Guangdong, Tianjin, for example, based on the cumulative number of confirmed diagnoses and the existing number of confirmed diagnoses to draw a line of four columns of pie charts.

<img width="416" alt="image" src="https://github.com/shuoyuwang/Data-visualization/assets/59498813/f649da2b-288d-485e-8a29-58c47bd72e3c">

10. Use the radar function of the pyecharts library to draw a radar chart based on the cumulative number of confirmed cases in Beijing, Shanghai, Guangdong, and Tianjin, for example.

<img width="416" alt="image" src="https://github.com/shuoyuwang/Data-visualization/assets/59498813/f185a72d-cac9-4b76-bc96-0967601929a4">

11. Use the radar function of the pyecharts library to draw a radar chart based on the number of existing diagnoses and the incremental number of existing diagnoses in Beijing, Shanghai, Guangdong, and Tianjin, for example.

<img width="416" alt="image" src="https://github.com/shuoyuwang/Data-visualization/assets/59498813/ba1db2c3-4e57-489e-ae5d-ee9866d4a44e">

12. Use wordcloud library to draw word cloud map based on domestic epidemic.

<img width="410" alt="image" src="https://github.com/shuoyuwang/Data-visualization/assets/59498813/beded7d5-6c02-4655-b0ef-06b309f5f94d">

13. Using the wordcloud library to draw a word cloud map based on foreign outbreaks.

<img width="416" alt="image" src="https://github.com/shuoyuwang/Data-visualization/assets/59498813/db8b8b84-b0b2-40df-8bc8-c5c9948962d0">

14. Use pyecharts library, map function to draw based on the cumulative number of diagnosed outbreaks in various provinces and cities in the country to map the epidemic.

(1) get_data.py to get data. Write get_data function to get the data, get_time function to get the update time, parse_data function to parse the data.

<img width="345" alt="image" src="https://github.com/shuoyuwang/Data-visualization/assets/59498813/c51066b6-e687-41e3-ba91-bf1cac7c1262">

(2) execution.py processes the extracted data. Create two lists and establish one-to-one correspondence.

<img width="364" alt="image" src="https://github.com/shuoyuwang/Data-visualization/assets/59498813/6b203aa5-1639-4251-aa1f-62d16dc5619e">

(3) map_draw.py draws the map. Use the map function of the pyecharts library to draw the map.

<img width="415" alt="image" src="https://github.com/shuoyuwang/Data-visualization/assets/59498813/db5b1bd0-dddb-4bfd-9c2c-23e44936767a">


