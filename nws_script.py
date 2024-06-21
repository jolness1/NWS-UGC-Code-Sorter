import sys


data = """
NM|201|ABQ|Northwest Plateau|NM201|McKinley|35031|M|nw|36.427|-108.4064
NM|201|ABQ|Northwest Plateau|NM201|San Juan|35045|M|nw|36.427|-108.4064
NM|202|ABQ|Chuska Mountains|NM202|McKinley|35031|M|nw|36.0409|-108.9296
NM|202|ABQ|Chuska Mountains|NM202|San Juan|35045|M|nw|36.0409|-108.9296
NM|203|ABQ|Far Northwest Highlands|NM203|Rio Arriba|35039|M|nc|36.6585|-107.1028
NM|203|ABQ|Far Northwest Highlands|NM203|Sandoval|35043|M|nc|36.6585|-107.1028
NM|203|ABQ|Far Northwest Highlands|NM203|San Juan|35045|M|nc|36.6585|-107.1028
NM|204|ABQ|Northwest Highlands|NM204|McKinley|35031|M|nc|36.0067|-107.5052
NM|204|ABQ|Northwest Highlands|NM204|Rio Arriba|35039|M|nc|36.0067|-107.5052
NM|204|ABQ|Northwest Highlands|NM204|Sandoval|35043|M|nc|36.0067|-107.5052
NM|204|ABQ|Northwest Highlands|NM204|San Juan|35045|M|nc|36.0067|-107.5052
NM|205|ABQ|West Central Plateau|NM205|Catron|35003|M|wc|35.0288|-108.817
NM|205|ABQ|West Central Plateau|NM205|Cibola|35006|M|wc|35.0288|-108.817
NM|205|ABQ|West Central Plateau|NM205|McKinley|35031|M|wc|35.0288|-108.817
NM|206|ABQ|West Central Mountains|NM206|Catron|35003|M|nc|35.0709|-108.0574
NM|206|ABQ|West Central Mountains|NM206|Cibola|35006|M|nc|35.0709|-108.0574
NM|206|ABQ|West Central Mountains|NM206|McKinley|35031|M|nc|35.0709|-108.0574
NM|206|ABQ|West Central Mountains|NM206|Sandoval|35043|M|nc|35.0709|-108.0574
NM|206|ABQ|West Central Mountains|NM206|Socorro|35053|M|nc|35.0709|-108.0574
NM|207|ABQ|West Central Highlands|NM207|Bernalillo|35001|M|nc|34.9677|-107.3538
NM|207|ABQ|West Central Highlands|NM207|Cibola|35006|M|nc|34.9677|-107.3538
NM|207|ABQ|West Central Highlands|NM207|McKinley|35031|M|nc|34.9677|-107.3538
NM|207|ABQ|West Central Highlands|NM207|Sandoval|35043|M|nc|34.9677|-107.3538
NM|207|ABQ|West Central Highlands|NM207|Socorro|35053|M|nc|34.9677|-107.3538
NM|207|ABQ|West Central Highlands|NM207|Valencia|35061|M|nc|34.9677|-107.3538
NM|208|ABQ|Southwest Mountains|NM208|Catron|35003|M|cc|33.8571|-108.317
NM|208|ABQ|Southwest Mountains|NM208|Socorro|35053|M|cc|33.8571|-108.317
NM|209|ABQ|San Francisco River Valley|NM209|Catron|35003|M|wc|33.509|-108.8601
NM|210|ABQ|Tusas Mountains Including Chama|NM210|Rio Arriba|35039|M|nc|36.7058|-106.2539
NM|210|ABQ|Tusas Mountains Including Chama|NM210|Taos|35055|M|nc|36.7058|-106.2539
NM|211|ABQ|Jemez Mountains|NM211|Los Alamos|35028|M|nc|35.9021|-106.5974
NM|211|ABQ|Jemez Mountains|NM211|Rio Arriba|35039|M|nc|35.9021|-106.5974
NM|211|ABQ|Jemez Mountains|NM211|Sandoval|35043|M|nc|35.9021|-106.5974
NM|212|ABQ|Glorieta Mesa Including Glorieta Pass|NM212|San Miguel|35047|M|nc|35.516|-105.694
NM|212|ABQ|Glorieta Mesa Including Glorieta Pass|NM212|Santa Fe|35049|M|nc|35.516|-105.694
NM|213|ABQ|Northern Sangre de Cristo Mountains|NM213|Colfax|35007|M|ne|36.7161|-105.3905
NM|213|ABQ|Northern Sangre de Cristo Mountains|NM213|Taos|35055|M|ne|36.7161|-105.3905
NM|214|ABQ|Southern Sangre de Cristo Mountains|NM214|Colfax|35007|M|nc|35.9865|-105.5998
NM|214|ABQ|Southern Sangre de Cristo Mountains|NM214|Mora|35033|M|nc|35.9865|-105.5998
NM|214|ABQ|Southern Sangre de Cristo Mountains|NM214|Rio Arriba|35039|M|nc|35.9865|-105.5998
NM|214|ABQ|Southern Sangre de Cristo Mountains|NM214|San Miguel|35047|M|nc|35.9865|-105.5998
NM|214|ABQ|Southern Sangre de Cristo Mountains|NM214|Santa Fe|35049|M|nc|35.9865|-105.5998
NM|214|ABQ|Southern Sangre de Cristo Mountains|NM214|Taos|35055|M|nc|35.9865|-105.5998
NM|215|ABQ|East Slopes Sangre de Cristo Mountains|NM215|Colfax|35007|M|ne|36.2296|-105.1554
NM|215|ABQ|East Slopes Sangre de Cristo Mountains|NM215|Mora|35033|M|ne|36.2296|-105.1554
NM|215|ABQ|East Slopes Sangre de Cristo Mountains|NM215|San Miguel|35047|M|ne|36.2296|-105.1554
NM|216|ABQ|Upper Rio Grande Valley|NM216|Rio Arriba|35039|M|nc|36.6232|-105.7524
NM|216|ABQ|Upper Rio Grande Valley|NM216|Taos|35055|M|nc|36.6232|-105.7524
NM|217|ABQ|Espanola Valley|NM217|Rio Arriba|35039|M|nc|36.1335|-106.0931
NM|217|ABQ|Espanola Valley|NM217|Santa Fe|35049|M|nc|36.1335|-106.0931
NM|217|ABQ|Espanola Valley|NM217|Taos|35055|M|nc|36.1335|-106.0931
NM|218|ABQ|Santa Fe Metro Area|NM218|Bernalillo|35001|M|nc|35.5304|-106.1074
NM|218|ABQ|Santa Fe Metro Area|NM218|Sandoval|35043|M|nc|35.5304|-106.1074
NM|218|ABQ|Santa Fe Metro Area|NM218|Santa Fe|35049|M|nc|35.5304|-106.1074
NM|219|ABQ|Middle Rio Grande Valley/Albuquerque Metro Area|NM219|Bernalillo|35001|M|nc|35.0023|-106.7444
NM|219|ABQ|Middle Rio Grande Valley/Albuquerque Metro Area|NM219|Cibola|35006|M|nc|35.0023|-106.7444
NM|219|ABQ|Middle Rio Grande Valley/Albuquerque Metro Area|NM219|Sandoval|35043|M|nc|35.0023|-106.7444
NM|219|ABQ|Middle Rio Grande Valley/Albuquerque Metro Area|NM219|Torrance|35057|M|nc|35.0023|-106.7444
NM|219|ABQ|Middle Rio Grande Valley/Albuquerque Metro Area|NM219|Valencia|35061|M|nc|35.0023|-106.7444
NM|220|ABQ|Lower Rio Grande Valley|NM220|Socorro|35053|M|cc|33.9223|-106.8008
NM|221|ABQ|Sandia/Manzano Mountains Including Edgewood|NM221|Bernalillo|35001|M|nc|34.9556|-106.3043
NM|221|ABQ|Sandia/Manzano Mountains Including Edgewood|NM221|Sandoval|35043|M|nc|34.9556|-106.3043
NM|221|ABQ|Sandia/Manzano Mountains Including Edgewood|NM221|Santa Fe|35049|M|nc|34.9556|-106.3043
NM|221|ABQ|Sandia/Manzano Mountains Including Edgewood|NM221|Torrance|35057|M|nc|34.9556|-106.3043
NM|221|ABQ|Sandia/Manzano Mountains Including Edgewood|NM221|Valencia|35061|M|nc|34.9556|-106.3043
NM|222|ABQ|Estancia Valley|NM222|Bernalillo|35001|M|nc|34.789|-105.9856
NM|222|ABQ|Estancia Valley|NM222|Santa Fe|35049|M|nc|34.789|-105.9856
NM|222|ABQ|Estancia Valley|NM222|Torrance|35057|M|nc|34.789|-105.9856
NM|223|ABQ|Central Highlands|NM223|San Miguel|35047|M|nc|34.8354|-105.5657
NM|223|ABQ|Central Highlands|NM223|Santa Fe|35049|M|nc|34.8354|-105.5657
NM|223|ABQ|Central Highlands|NM223|Torrance|35057|M|nc|34.8354|-105.5657
NM|224|ABQ|South Central Highlands|NM224|Lincoln|35027|M|cc|34.1329|-106.1646
NM|224|ABQ|South Central Highlands|NM224|Socorro|35053|M|cc|34.1329|-106.1646
NM|224|ABQ|South Central Highlands|NM224|Torrance|35057|M|cc|34.1329|-106.1646
NM|224|ABQ|South Central Highlands|NM224|Valencia|35061|M|cc|34.1329|-106.1646
NM|225|ABQ|Upper Tularosa Valley|NM225|Lincoln|35027|M|cc|33.6587|-106.0398
NM|225|ABQ|Upper Tularosa Valley|NM225|Socorro|35053|M|cc|33.6587|-106.0398
NM|226|ABQ|South Central Mountains|NM226|Lincoln|35027|M|cc|33.5868|-105.5869
NM|227|ABQ|Johnson and Bartlett Mesas Including Raton Pass|NM227|Colfax|35007|M|ne|36.7769|-104.3106
NM|227|ABQ|Johnson and Bartlett Mesas Including Raton Pass|NM227|Union|35059|M|ne|36.7769|-104.3106
NM|228|ABQ|Far Northeast Highlands|NM228|Colfax|35007|M|ne|36.256|-104.5899
NM|228|ABQ|Far Northeast Highlands|NM228|Mora|35033|M|ne|36.256|-104.5899
NM|229|ABQ|Northeast Highlands|NM229|San Miguel|35047|M|ne|35.5317|-105.0208
NM|230|ABQ|Union County|NM230|Union|35059|M|ne|36.4519|-103.4227
NM|231|ABQ|Harding County|NM231|Harding|35021|M|ne|35.858|-103.8199
NM|232|ABQ|Eastern San Miguel County|NM232|San Miguel|35047|M|ne|35.4457|-104.2579
NM|233|ABQ|Guadalupe County|NM233|Guadalupe|35019|M|ec|34.8633|-104.7907
NM|234|ABQ|Quay County|NM234|Quay|35037|M|ec|35.1043|-103.5497
NM|235|ABQ|Curry County|NM235|Curry|35009|M|ec|34.5741|-103.3468
NM|236|ABQ|Roosevelt County|NM236|Roosevelt|35041|M|ec|34.0213|-103.4802
NM|237|ABQ|De Baca County|NM237|De Baca|35011|M|ec|34.3424|-104.412
NM|238|ABQ|Chaves County Plains|NM238|Chaves|35005|M|se|33.498|-104.3114
NM|239|ABQ|Eastern Lincoln County|NM239|Lincoln|35027|M|cc|33.7904|-105.1628
NM|240|ABQ|Southwest Chaves County|NM240|Chaves|35005|M|se|32.8182|-105.0963
NM|241|ABQ|San Agustin Plains and Adjacent Lowlands|NM241|Catron|35003|M|cc|33.9792|-107.5332
NM|241|ABQ|San Agustin Plains and Adjacent Lowlands|NM241|Socorro|35053|M|cc|33.9792|-107.5332
MN|039|ABR|Traverse|MN039|Traverse|27155|C|wc|45.7721|-96.4716
MN|046|ABR|Big Stone|MN046|Big Stone|27011|C|wc|45.4261|-96.411
SD|003|ABR|Corson|SD003|Corson|46031|M|nc|45.7087|-101.1969
SD|004|ABR|Campbell|SD004|Campbell|46021|C|nc|45.7711|-100.0517
SD|005|ABR|McPherson|SD005|McPherson|46089|C|nc|45.7664|-99.2215
SD|006|ABR|Brown|SD006|Brown|46013|C|ne|45.5898|-98.3516
SD|007|ABR|Marshall|SD007|Marshall|46091|C|ne|45.7586|-97.5986
SD|008|ABR|Roberts|SD008|Roberts|46109|C|ne|45.6296|-96.9461
SD|009|ABR|Walworth|SD009|Walworth|46129|C|nc|45.4299|-100.0316
SD|010|ABR|Edmunds|SD010|Edmunds|46045|C|nc|45.4188|-99.2156
SD|011|ABR|Day|SD011|Day|46037|C|ne|45.3672|-97.6075
SD|015|ABR|Dewey|SD015|Dewey|46041|M|nc|45.1566|-100.8719
SD|016|ABR|Potter|SD016|Potter|46107|C|nc|45.0645|-99.9573
SD|017|ABR|Faulk|SD017|Faulk|46049|C|nc|45.0711|-99.1453
SD|018|ABR|Spink|SD018|Spink|46115|C|ne|44.9381|-98.3463
SD|019|ABR|Clark|SD019|Clark|46025|C|ne|44.8582|-97.7295
SD|020|ABR|Codington|SD020|Codington|46029|C|ne|44.9778|-97.1886
SD|021|ABR|Grant|SD021|Grant|46051|C|ne|45.172|-96.7678
SD|022|ABR|Hamlin|SD022|Hamlin|46057|C|ne|44.6737|-97.1883
SD|023|ABR|Deuel|SD023|Deuel|46039|C|ne|44.76|-96.668
SD|033|ABR|Stanley|SD033|Stanley|46117|CM|cc|44.4123|-100.7359
SD|034|ABR|Sully|SD034|Sully|46119|C|cc|44.7155|-100.1322
SD|035|ABR|Hughes|SD035|Hughes|46065|C|cc|44.389|-99.9961
SD|036|ABR|Hyde|SD036|Hyde|46069|C|cc|44.5474|-99.4871
SD|037|ABR|Hand|SD037|Hand|46059|C|cc|44.5478|-99.005
SD|045|ABR|Jones|SD045|Jones|46075|C|cc|43.9604|-100.6896
SD|048|ABR|Lyman|SD048|Lyman|46085|C|cc|43.8958|-99.8474
SD|051|ABR|Buffalo|SD051|Buffalo|46017|C|cc|44.0763|-99.205
AK|102|AFC|Anchorage |AK102|Anchorage|02020|A||61.2292|-149.3466
AK|103|AFC|East Turnagain Arm |AK103|Anchorage|02020|A||61.0377|-148.7761
AK|112|AFC|Matanuska Valley |AK112|Matanuska-Susitna|02170|A||61.6518|-149.2037
AK|121|AFC|Western Kenai Peninsula|AK121|Kenai Peninsula|02122|A||60.3254|-150.709
AK|126|AFC|Western Prince William Sound |AK126|Kenai Peninsula|02122|A||60.3278|-149.0357
AK|126|AFC|Western Prince William Sound |AK126|Chugach|02063|A||60.3278|-149.0357
AK|132|AFC|Northeast Prince William Sound |AK132|Chugach|02063|A||61.11|-146.3052
AK|135|AFC|Southeast Prince William Sound|AK135|Chugach|02063|A||60.5285|-144.9344
AK|142|AFC|Copper River Basin |AK142|Matanuska-Susitna|02170|A||61.9431|-144.7751
AK|142|AFC|Copper River Basin |AK142|Copper River|02066|A||61.9431|-144.7751
AK|142|AFC|Copper River Basin |AK142|Chugach|02063|A||61.9431|-144.7751
AK|145|AFC|Susitna Valley|AK145|Bethel|02050|A||62.0904|-150.7335
AK|145|AFC|Susitna Valley|AK145|Kenai Peninsula|02122|A||62.0904|-150.7335
AK|145|AFC|Susitna Valley|AK145|Matanuska-Susitna|02170|A||62.0904|-150.7335
AK|152|AFC|Lower Kuskokwim Valley|AK152|Bethel|02050|A||61.4395|-156.4803
AK|152|AFC|Lower Kuskokwim Valley|AK152|Dillingham|02070|A||61.4395|-156.4803
AK|152|AFC|Lower Kuskokwim Valley|AK152|Kenai Peninsula|02122|A||61.4395|-156.4803
AK|152|AFC|Lower Kuskokwim Valley|AK152|Lake and Peninsula|02164|A||61.4395|-156.4803
AK|152|AFC|Lower Kuskokwim Valley|AK152|Matanuska-Susitna|02170|A||61.4395|-156.4803
AK|155|AFC|Kuskokwim Delta|AK155|Bethel|02050|A||60.6404|-162.6305
AK|161|AFC|Bristol Bay|AK161|Bethel|02050|A||59.2984|-157.2451
AK|161|AFC|Bristol Bay|AK161|Bristol Bay|02060|A||59.2984|-157.2451
AK|161|AFC|Bristol Bay|AK161|Dillingham|02070|A||59.2984|-157.2451
AK|161|AFC|Bristol Bay|AK161|Kenai Peninsula|02122|A||59.2984|-157.2451
AK|161|AFC|Bristol Bay|AK161|Kodiak Island|02150|A||59.2984|-157.2451
AK|161|AFC|Bristol Bay|AK161|Lake and Peninsula|02164|A||59.2984|-157.2451
AK|171|AFC|Kodiak Island|AK171|Kenai Peninsula|02122|A||58.2911|-154.1629
AK|171|AFC|Kodiak Island|AK171|Kodiak Island|02150|A||58.2911|-154.1629
AK|171|AFC|Kodiak Island|AK171|Lake and Peninsula|02164|A||58.2911|-154.1629
AK|181|AFC|Alaska Peninsula|AK181|Aleutians East|02013|A||55.6116|-161.2034
AK|181|AFC|Alaska Peninsula|AK181|Lake and Peninsula|02164|A||55.6096|-161.2034
AK|185|AFC|Eastern Aleutians|AK185|Aleutians West|02016|AH||53.5983|-167.2049
AK|187|AFC|Central Aleutians|AK187|Aleutians West|02016|AH||52.0613|-175.0715
AK|191|AFC|Western Aleutians|AK191|Aleutians West|02016|AH||52.3658|175.5393
AK|195|AFC|Pribilof Islands|AK195|Aleutians West|02016|AH||56.9092|-169.979
AK|801|AFG|Western Arctic Coast|AK801|North Slope|02185|A||69.0125|-164.1064
AK|802|AFG|Northwest Arctic Coast|AK802|North Slope|02185|A||70.3019|-159.508
AK|803|AFG|Northern Arctic Coast|AK803|North Slope|02185|A||70.6873|-155.3712
AK|804|AFG|Central Beaufort Sea Coast|AK804|North Slope|02185|A||70.2069|-149.5617
AK|805|AFG|Eastern Beaufort Sea Coast|AK805|North Slope|02185|A||69.8543|-144.0064
AK|806|AFG|Western Arctic Plains|AK806|North Slope|02185|A||69.4448|-157.04
AK|807|AFG|Howard Pass and the Delong Mountains|AK807|North Slope|02185|A||68.4515|-159.5118
AK|808|AFG|Central Arctic Plains|AK808|North Slope|02185|A||69.3952|-150.0441
AK|809|AFG|Central Brooks Range|AK809|North Slope|02185|A||68.4522|-151.0083
AK|810|AFG|Romanzof Mountains|AK810|North Slope|02185|A||68.9538|-144.9059
AK|811|AFG|South Slopes of the Eastern Brooks Range|AK811|Yukon-Koyukuk|02290|A||67.8471|-144.9201
AK|812|AFG|South Slopes of the Central Brooks Range|AK812|Yukon-Koyukuk|02290|A||67.5646|-151.9607
AK|813|AFG|South Slopes of the Western Brooks Range|AK813|Northwest Arctic|02188|A||67.6243|-157.2881
AK|814|AFG|Noatak Valley|AK814|Northwest Arctic|02188|A||67.6896|-161.9337
AK|815|AFG|Kivalina and Red Dog Dock|AK815|Northwest Arctic|02188|A||67.6038|-164.1586
AK|816|AFG|Lower Kobuk Valley|AK816|Northwest Arctic|02188|A||66.7012|-160.5806
AK|817|AFG|Baldwin Peninsula|AK817|Northwest Arctic|02188|A||66.5619|-161.7133
AK|818|AFG|Northern Seward Peninsula|AK818|Northwest Arctic|02188|A||65.865|-161.6971
AK|819|AFG|Upper Kobuk Valleys|AK819|Northwest Arctic|02188|A||66.775|-157.3858
AK|820|AFG|Shishmaref|AK820|Nome|02180|A||66.117|-165.867
AK|821|AFG|Bering Strait Coast|AK821|Nome|02180|A||65.4254|-166.6301
AK|822|AFG|Southern Seward Peninsula Coast|AK822|Nome|02180|A||64.6146|-164.4871
AK|823|AFG|Interior Seward Peninsula|AK823|Nome|02180|A||65.2674|-163.7888
AK|824|AFG|Eastern Norton Sound and Nulato Hills|AK824|Nome|02180|A||64.2108|-160.884
AK|825|AFG|Yukon Delta Coast|AK825|Kusilvak|02158|A||62.1513|-164.2464
AK|826|AFG|Lower Yukon River|AK826|Kusilvak|02158|A||62.1612|-162.0465
AK|827|AFG|St. Lawrence Island|AK827|Nome|02180|A||63.3895|-170.3421
AK|828|AFG|Lower Koyukuk Valley|AK828|Yukon-Koyukuk|02290|A||65.6681|-156.8481
AK|829|AFG|Middle Yukon Valley|AK829|Yukon-Koyukuk|02290|A||64.4694|-156.776
AK|830|AFG|Lower Yukon and Innoko Valleys|AK830|Yukon-Koyukuk|02290|A||63.0674|-158.329
AK|831|AFG|Upper Koyukuk Valley|AK831|Yukon-Koyukuk|02290|A||66.3527|-152.8907
AK|832|AFG|Dalton Highway Summits|AK832|Yukon-Koyukuk|02290|A||66.3044|-150.2855
AK|833|AFG|Yukon Flats|AK833|Yukon-Koyukuk|02290|A||66.5038|-144.6111
AK|834|AFG|White Mountains and High Terrain South of the Yukon River|AK834|Yukon-Koyukuk|02290|A||65.4537|-146.8278
AK|835|AFG|Fortymile Country|AK835|Southeast Fairbanks|02240|A||64.351|-142.5474
AK|836|AFG|Upper Tanana Valley|AK836|Southeast Fairbanks|02240|A||63.0016|-142.528
AK|837|AFG|Delta Junction|AK837|Southeast Fairbanks|02240|A||64.0671|-145.6603
AK|838|AFG|Upper Chena River Valley|AK838|Fairbanks North Star|02090|A||64.8329|-145.4109
AK|839|AFG|Tanana Flats|AK839|Fairbanks North Star|02090|A||64.4858|-147.58
AK|840|AFG|Eielson Air Force Base and Salcha|AK840|Fairbanks North Star|02090|A||64.5731|-146.8032
AK|841|AFG|Goldstream Valley and Nenana Hills|AK841|Fairbanks North Star|02090|A||64.8226|-148.4043
AK|842|AFG|Chatanika River Valley|AK842|Fairbanks North Star|02090|A||65.1455|-147.4888
AK|843|AFG|Two Rivers|AK843|Fairbanks North Star|02090|A||64.915|-146.8659
AK|844|AFG|Fairbanks Metro Area|AK844|Fairbanks North Star|02090|A||64.8465|-147.68
AK|845|AFG|Nenana|AK845|Yukon-Koyukuk|02290|A||64.5373|-148.7871
AK|846|AFG|Central Interior|AK846|Yukon-Koyukuk|02290|A||64.7511|-151.8283
AK|847|AFG|Northern Denali Borough|AK847|Denali|02068|A||63.8161|-150.0994
AK|848|AFG|Southern Denali Borough|AK848|Denali|02068|A||63.3248|-149.7848
AK|849|AFG|Eastern Alaska Range North of Trims Camp|AK849|Southeast Fairbanks|02240|A||63.7236|-145.7753
AK|850|AFG|Eastern Alaska Range South of Trims Camp|AK850|Southeast Fairbanks|02240|A||63.3137|-145.1121
AK|851|AFG|North Slopes of the Western Alaska Range|AK851|Yukon-Koyukuk|02290|A||62.5083|-153.8608
AK|852|AFG|Upper Kuskokwim Valley|AK852|Yukon-Koyukuk|02290|A||62.8537|-155.2228
AK|317|AJK|City and Borough of Yakutat|AK317|Yakutat|02282|A||59.9007|-140.4
AK|318|AJK|Municipality of Skagway|AK318|Skagway|02230|A||59.5634|-135.3363
AK|319|AJK|Haines Borough and Klukwan|AK319|Haines|02100|A||59.1231|-135.5029
AK|320|AJK|Glacier Bay|AK320|Hoonah-Angoon|02105|A||58.7919|-136.374
AK|321|AJK|Eastern Chichagof Island|AK321|Hoonah-Angoon|02105|A||58.0322|-135.5308
AK|322|AJK|Cape Fairweather to Lisianski Strait|AK322|Hoonah-Angoon|02105|A||58.3895|-136.9144
AK|323|AJK|City and Borough of Sitka|AK323|Sitka|02220|A||57.2368|-135.3018
AK|324|AJK|Admiralty Island|AK324|Hoonah-Angoon|02105|A||57.7037|-134.0857
AK|325|AJK|City and Borough of Juneau|AK325|Juneau|02110|A||58.4584|-134.1787
AK|326|AJK|Petersburg Borough|AK326|Petersburg Borough|02195|A||57.1338|-132.9279
AK|327|AJK|Western Kupreanof and Kuiu Island|AK327|Prince of Wales-Hyder|02198|A||56.6439|-133.8989
AK|328|AJK|Prince of Wales Island|AK328|Prince of Wales-Hyder|02198|A||55.5002|-132.8808
AK|329|AJK|City and Borough of Wrangell|AK329|Wrangell|02275|A||56.3326|-132.0115
AK|330|AJK|Ketchikan Gateway Borough|AK330|Ketchikan|02130|A||55.597|-130.9302
AK|331|AJK|City of Hyder|AK331|Prince of Wales-Hyder|02198|A||55.9569|-130.1734
AK|332|AJK|Annette Island|AK332|Prince of Wales-Hyder|02198|A||55.1277|-131.4853
MD|021|AKQ|Dorchester|MD021|Dorchester|24019|E|se|38.4799|-76.008
MD|022|AKQ|Wicomico|MD022|Wicomico|24045|E|se|38.3737|-75.6193
MD|023|AKQ|Somerset|MD023|Somerset|24039|E|se|38.1188|-75.7449
MD|024|AKQ|Inland Worcester|MD024|Worcester|24047|E|se|38.2142|-75.3833
MD|025|AKQ|Maryland Beaches|MD025|Worcester|24047|E|se|38.251|-75.1598
NC|012|AKQ|Northampton|NC012|Northampton|37131|E|ne|36.4177|-77.3967
NC|013|AKQ|Hertford|NC013|Hertford|37091|E|ne|36.359|-76.9838
NC|014|AKQ|Gates|NC014|Gates|37073|E|ne|36.4444|-76.7017
NC|015|AKQ|Pasquotank|NC015|Pasquotank|37139|E|ne|36.2974|-76.2867
NC|016|AKQ|Camden|NC016|Camden|37029|E|ne|36.3902|-76.2101
NC|017|AKQ|Western Currituck|NC017|Currituck|37053|E|ne|36.4012|-76.034
NC|030|AKQ|Bertie|NC030|Bertie|37015|E|ne|36.0662|-76.9791
NC|031|AKQ|Chowan|NC031|Chowan|37041|E|ne|36.1507|-76.608
NC|032|AKQ|Perquimans|NC032|Perquimans|37143|E|ne|36.2069|-76.4419
NC|102|AKQ|Eastern Currituck|NC102|Currituck|37053|E|ne|36.4001|-75.844
VA|048|AKQ|Fluvanna|VA048|Fluvanna|51065|E|cc|37.8419|-78.2774
VA|060|AKQ|Prince Edward|VA060|Prince Edward|51147|E|cc|37.2243|-78.4411
VA|061|AKQ|Cumberland|VA061|Cumberland|51049|E|cc|37.512|-78.245
VA|062|AKQ|Goochland|VA062|Goochland|51075|E|cc|37.722|-77.9164
VA|064|AKQ|Caroline|VA064|Caroline|51033|E|nc|38.0272|-77.3475
VA|065|AKQ|Mecklenburg|VA065|Mecklenburg|51117|E|sc|36.6804|-78.3627
VA|066|AKQ|Lunenburg|VA066|Lunenburg|51111|E|sc|36.9462|-78.2406
VA|067|AKQ|Nottoway|VA067|Nottoway|51135|E|sc|37.1431|-78.0512
VA|068|AKQ|Amelia|VA068|Amelia|51007|E|cc|37.336|-77.9761
VA|069|AKQ|Powhatan|VA069|Powhatan|51145|E|cc|37.5502|-77.9152
VA|075|AKQ|Westmoreland|VA075|Westmoreland|51193|E|ec|38.1108|-76.8052
VA|075|AKQ|Westmoreland|VA075|Westmoreland|51193|E|ec|38.1366|-76.7253
VA|076|AKQ|Richmond|VA076|Richmond|51159|E|ec|37.8881|-76.7671
VA|076|AKQ|Richmond|VA076|Richmond|51159|E|ec|37.9429|-76.7249
VA|077|AKQ|Northumberland|VA077|Northumberland|51133|E|ee|37.8863|-76.4228
VA|078|AKQ|Lancaster|VA078|Lancaster|51103|E|ee|37.6779|-76.4808
VA|078|AKQ|Lancaster|VA078|Lancaster|51103|E|ee|37.7371|-76.465
VA|079|AKQ|Brunswick|VA079|Brunswick|51025|E|sc|36.7648|-77.859
VA|080|AKQ|Dinwiddie|VA080|Dinwiddie|51053|E|sc|37.0759|-77.6323
VA|081|AKQ|Prince George|VA081|Prince George|51149|E|sc|37.1915|-77.2389
VA|081|AKQ|Prince George|VA081|City of Hopewell|51670|E|sc|37.1915|-77.2389
VA|081|AKQ|Prince George|VA081|City of Petersburg|51730|E|sc|37.1915|-77.2389
VA|082|AKQ|Charles City|VA082|Charles City|51036|E|ec|37.2385|-76.9027
VA|082|AKQ|Charles City|VA082|Charles City|51036|E|ec|37.3565|-77.0613
VA|083|AKQ|New Kent|VA083|New Kent|51127|E|ec|37.5052|-76.9972
VA|084|AKQ|Gloucester|VA084|Gloucester|51073|E|ee|37.3249|-76.5063
VA|084|AKQ|Gloucester|VA084|Gloucester|51073|E|se|37.4257|-76.5431
VA|085|AKQ|Middlesex|VA085|Middlesex|51119|E|ee|37.6258|-76.4816
VA|085|AKQ|Middlesex|VA085|Middlesex|51119|E|ee|37.6353|-76.5769
VA|086|AKQ|Mathews|VA086|Mathews|51115|E|ee|37.4368|-76.3444
VA|086|AKQ|Mathews|VA086|Mathews|51115|E|ee|37.4577|-76.3416
VA|087|AKQ|Greensville|VA087|Greensville|51081|E|sc|36.6763|-77.559
VA|087|AKQ|Greensville|VA087|City of Emporia|51595|E|se|36.6763|-77.559
VA|088|AKQ|Sussex|VA088|Sussex|51183|E|se|36.9218|-77.2618
VA|089|AKQ|Surry|VA089|Surry|51181|E|se|37.1169|-76.8883
VA|090|AKQ|James City|VA090|James City|51095|E|se|37.2088|-76.7412
VA|090|AKQ|James City|VA090|James City|51095|E|se|37.3264|-76.7745
VA|090|AKQ|James City|VA090|City of Williamsburg|51830|E|se|37.3264|-76.7745
VA|092|AKQ|Southampton|VA092|Southampton|51175|E|se|36.7199|-77.1038
VA|092|AKQ|Southampton|VA092|City of Franklin|51620|E|se|36.7199|-77.1038
VA|093|AKQ|Isle of Wight|VA093|Isle of Wight|51093|E|se|36.9067|-76.7091
VA|095|AKQ|Norfolk/Portsmouth|VA095|City of Norfolk|51710|E|se|36.8752|-76.2937
VA|095|AKQ|Norfolk/Portsmouth|VA095|City of Norfolk|51710|E|se|36.8959|-76.3428
VA|095|AKQ|Norfolk/Portsmouth|VA095|City of Portsmouth|51740|E|se|36.8752|-76.2937
VA|095|AKQ|Norfolk/Portsmouth|VA095|City of Portsmouth|51740|E|se|36.8959|-76.3428
VA|096|AKQ|Suffolk|VA096|City of Suffolk|51800|E|se|36.6926|-76.6417
VA|096|AKQ|Suffolk|VA096|City of Suffolk|51800|E|se|36.8935|-76.4749
VA|097|AKQ|Chesapeake|VA097|City of Chesapeake|51550|E|se|36.6778|-76.3024
VA|098|AKQ|Virginia Beach|VA098|City of Virginia Beach|51810|E|se|36.7494|-76.0571
VA|099|AKQ|Accomack|VA099|Accomack|51001|E|se|37.7659|-75.6472
VA|100|AKQ|Northampton|VA100|Northampton|51131|E|ee|37.3566|-75.8995
VA|509|AKQ|Western Louisa|VA509|Louisa|51109|E|cc|38.0408|-78.1061
VA|510|AKQ|Eastern Louisa|VA510|Louisa|51109|E|cc|37.9335|-77.8608
VA|511|AKQ|Western Hanover|VA511|Hanover|51085|E|cc|37.809|-77.5823
VA|512|AKQ|Eastern Hanover|VA512|Hanover|51085|E|cc|37.4671|-77.2793
VA|513|AKQ|Western Chesterfield|VA513|Chesterfield|51041|E|cc|37.3765|-77.5835
VA|514|AKQ|Eastern Chesterfield (Including Col. Heights)|VA514|City of Colonial Heights|51570|E|cc|37.3765|-77.5835
VA|515|AKQ|Western Henrico (Including the City of Richmond)|VA515|Henrico|51087|E|cc|37.5362|-77.42
VA|515|AKQ|Western Henrico (Including the City of Richmond)|VA515|City of Richmond|51760|E|cc|37.5293|-77.4754
VA|516|AKQ|Eastern Henrico|VA516|Henrico|51087|E|cc|37.5362|-77.42
VA|517|AKQ|Western King William|VA517|King William|51101|E|ec|37.7067|-77.0884
VA|518|AKQ|Eastern King William|VA518|King William|51101|E|ec|37.7067|-77.0884
VA|519|AKQ|Western King and Queen|VA519|King and Queen|51097|E|ec|37.7179|-76.8946
VA|520|AKQ|Eastern King and Queen|VA520|King and Queen|51097|E|ec|37.7179|-76.8946
VA|521|AKQ|Western Essex|VA521|Essex|51057|E|ec|37.8958|-76.808
VA|522|AKQ|Eastern Essex|VA522|Essex|51057|E|ec|37.9426|-76.9518
VA|523|AKQ|York|VA523|York|51199|E|se|37.2242|-76.5383
VA|523|AKQ|York|VA523|York|51199|E|se|37.256|-76.5124
VA|523|AKQ|York|VA523|City of Poquoson|51735|E|se|37.2242|-76.5383
VA|524|AKQ|Newport News/Hampton|VA524|City of Newport News|51700|e|SE|37.077|-76.5058
VA|525|AKQ|Hampton/Poquoson|VA525|City of Hampton|51650|E|se|37.0534|-76.3673
CT|001|ALY|Northern Litchfield|CT001|Litchfield|09005|E|nn|41.8851|-73.2502
CT|013|ALY|Southern Litchfield|CT013|Litchfield|09005|E|nn|41.6344|-73.2368
MA|001|ALY|Northern Berkshire|MA001|Berkshire|25003|E|ww|42.56|-73.1518
MA|025|ALY|Southern Berkshire|MA025|Berkshire|25003|E|ww|42.2158|-73.2511
NY|032|ALY|Northern Herkimer|NY032|Herkimer|36043|E|ee|43.7111|-74.9693
NY|033|ALY|Hamilton|NY033|Hamilton|36041|E|ee|43.6611|-74.4973
NY|038|ALY|Southern Herkimer|NY038|Herkimer|36043|E|ee|43.0923|-74.9549
NY|039|ALY|Southern Fulton|NY039|Fulton|36035|E|ee|43.0404|-74.4213
NY|040|ALY|Montgomery|NY040|Montgomery|36057|E|ee|42.9023|-74.4397
NY|041|ALY|Northern Saratoga|NY041|Saratoga|36091|E|ec|43.1808|-73.8582
NY|042|ALY|Northern Warren|NY042|Warren|36113|E|ec|43.5976|-73.8646
NY|043|ALY|Northern Washington|NY043|Washington|36115|E|ec|43.5196|-73.4239
NY|047|ALY|Schoharie|NY047|Schoharie|36095|E|ec|42.5882|-74.4421
NY|048|ALY|Western Schenectady|NY048|Schenectady|36093|E|ec|42.79|-74.1561
NY|049|ALY|Eastern Schenectady|NY049|Schenectady|36093|E|ec|42.8421|-73.9758
NY|050|ALY|Southern Saratoga|NY050|Saratoga|36091|E|ec|42.9413|-73.8768
NY|051|ALY|Western Albany|NY051|Albany|36001|E|ec|42.5646|-74.125
NY|052|ALY|Eastern Albany|NY052|Albany|36001|E|ec|42.6223|-73.8796
NY|053|ALY|Western Rensselaer|NY053|Rensselaer|36083|E|ec|42.7053|-73.6159
NY|054|ALY|Eastern Rensselaer|NY054|Rensselaer|36083|E|ec|42.7167|-73.4058
NY|058|ALY|Western Greene|NY058|Greene|36039|E|ec|42.257|-74.2376
NY|059|ALY|Eastern Greene|NY059|Greene|36039|E|ec|42.312|-73.9147
NY|060|ALY|Western Columbia|NY060|Columbia|36021|E|ec|42.2451|-73.733
NY|061|ALY|Eastern Columbia|NY061|Columbia|36021|E|ec|42.2548|-73.536
NY|063|ALY|Western Ulster|NY063|Ulster|36111|E|ec|41.9216|-74.3795
NY|064|ALY|Eastern Ulster|NY064|Ulster|36111|E|ec|41.8336|-74.0616
NY|065|ALY|Western Dutchess|NY065|Dutchess|36027|E|ec|41.7716|-73.8457
NY|066|ALY|Eastern Dutchess|NY066|Dutchess|36027|E|ec|41.7574|-73.6193
NY|082|ALY|Northern Fulton|NY082|Fulton|36035|E|ee|43.1615|-74.4228
NY|083|ALY|Southeast Warren|NY083|Warren|36113|E|ec|43.3468|-73.7376
NY|084|ALY|Southern Washington|NY084|Washington|36115|E|ec|43.1564|-73.436
VT|013|ALY|Bennington|VT013|Bennington|50003|E|ss|43.0355|-73.0929
VT|014|ALY|Western Windham|VT014|Windham|50025|E|ss|43.0015|-72.7867
VT|015|ALY|Eastern Windham|VT015|Windham|50025|E|ss|42.9675|-72.5583
OK|001|AMA|Cimarron|OK001|Cimarron|40025|C|pa|36.7483|-102.5178
OK|002|AMA|Texas|OK002|Texas|40139|C|pa|36.7479|-101.49
OK|003|AMA|Beaver|OK003|Beaver|40007|C|pa|36.7497|-100.4767
TX|001|AMA|Dallam|TX001|Dallam|48111|C|pa|36.2779|-102.6022
TX|002|AMA|Sherman|TX002|Sherman|48421|C|pa|36.2777|-101.8935
TX|003|AMA|Hansford|TX003|Hansford|48195|C|pa|36.2775|-101.3545
TX|004|AMA|Ochiltree|TX004|Ochiltree|48357|C|pa|36.2784|-100.8156
TX|005|AMA|Lipscomb|TX005|Lipscomb|48295|C|pa|36.2777|-100.2731
TX|006|AMA|Hartley|TX006|Hartley|48205|C|pa|35.84|-102.6029
TX|007|AMA|Moore|TX007|Moore|48341|C|pa|35.8377|-101.8929
TX|008|AMA|Hutchinson|TX008|Hutchinson|48233|C|pa|35.84|-101.3547
TX|009|AMA|Roberts|TX009|Roberts|48393|C|pa|35.8385|-100.8134
TX|010|AMA|Hemphill|TX010|Hemphill|48211|C|pa|35.8376|-100.2705
TX|011|AMA|Oldham|TX011|Oldham|48359|C|pa|35.405|-102.6029
TX|012|AMA|Potter|TX012|Potter|48375|C|pa|35.4013|-101.894
TX|013|AMA|Carson|TX013|Carson|48065|C|pa|35.4035|-101.3542
TX|014|AMA|Gray|TX014|Gray|48179|C|pa|35.4012|-100.8126
TX|015|AMA|Wheeler|TX015|Wheeler|48483|C|pa|35.4013|-100.2697
TX|016|AMA|Deaf Smith|TX016|Deaf Smith|48117|C|pa|34.966|-102.6049
TX|017|AMA|Randall|TX017|Randall|48381|C|pa|34.9669|-101.9073
TX|018|AMA|Armstrong|TX018|Armstrong|48011|C|pa|34.9649|-101.3574
TX|019|AMA|Donley|TX019|Donley|48129|C|pa|34.9654|-100.814
TX|020|AMA|Collingsworth|TX020|Collingsworth|48087|C|pa|34.9649|-100.2701
TX|317|AMA|Palo Duro Canyon|TX317|Randall|48381|C|pa|34.9436|-101.6778
MI|016|APX|Emmet|MI016|Emmet|26047|E|nn|45.5205|-84.8905
MI|017|APX|Cheboygan|MI017|Cheboygan|26031|E|nn|45.4468|-84.4999
MI|018|APX|Presque Isle|MI018|Presque Isle|26141|E|nn|45.3396|-83.9159
MI|020|APX|Leelanau|MI020|Leelanau|26089|E|nn|44.9367|-85.8123
MI|021|APX|Antrim|MI021|Antrim|26009|E|nn|45.0003|-85.1377
MI|022|APX|Otsego|MI022|Otsego|26137|E|nn|45.0214|-84.5988
MI|023|APX|Montmorency|MI023|Montmorency|26119|E|nn|45.0275|-84.1273
MI|024|APX|Alpena|MI024|Alpena|26007|E|nn|45.0347|-83.6285
MI|025|APX|Benzie|MI025|Benzie|26019|E|nn|44.6395|-86.0158
MI|026|APX|Grand Traverse|MI026|Grand Traverse|26055|E|nn|44.6709|-85.559
MI|027|APX|Kalkaska|MI027|Kalkaska|26079|E|nn|44.6846|-85.0902
MI|028|APX|Crawford|MI028|Crawford|26039|E|nn|44.6836|-84.6103
MI|029|APX|Oscoda|MI029|Oscoda|26135|E|nn|44.6817|-84.1297
MI|030|APX|Alcona|MI030|Alcona|26001|E|nn|44.6854|-83.5938
MI|031|APX|Manistee|MI031|Manistee|26101|E|nn|44.3332|-86.0571
MI|032|APX|Wexford|MI032|Wexford|26165|E|nn|44.3384|-85.5785
MI|033|APX|Missaukee|MI033|Missaukee|26113|E|nn|44.3373|-85.0947
MI|034|APX|Roscommon|MI034|Roscommon|26143|E|nn|44.3356|-84.6116
MI|035|APX|Ogemaw|MI035|Ogemaw|26129|E|nn|44.3349|-84.1266
MI|036|APX|Iosco|MI036|Iosco|26069|E|nn|44.3559|-83.636
MI|041|APX|Gladwin|MI041|Gladwin|26051|E|nn|43.9906|-84.3882
MI|042|APX|Arenac|MI042|Arenac|26011|E|nn|44.0656|-83.8948
MI|086|APX|Western Chippewa |MI086|Chippewa|26033|E|ee|46.3926|-84.9529
MI|087|APX|Central Chippewa |MI087|Chippewa|26033|E|ee|46.3221|-84.3611
MI|088|APX|Southeast Chippewa |MI088|Chippewa|26033|E|ee|46.0374|-83.9354
MI|095|APX|Western Mackinac |MI095|Mackinac|26097|E|ee|46.1362|-85.5266
MI|096|APX|Eastern Mackinac |MI096|Mackinac|26097|E|ee|46.0504|-84.7048
MI|097|APX|Mackinac Island/Bois Blanc Island |MI097|Mackinac|26097|E|ee|45.779|-84.4809
MI|098|APX|Beaver Island |MI098|Charlevoix|26029|E|nn|45.6807|-85.55
MI|099|APX|Charlevoix |MI099|Charlevoix|26029|E|nn|45.2247|-85.0407
IA|008|ARX|Mitchell|IA008|Mitchell|19131|C|nc|43.3564|-92.7891
IA|009|ARX|Howard|IA009|Howard|19089|C|ne|43.3568|-92.3172
IA|010|ARX|Winneshiek|IA010|Winneshiek|19191|C|ne|43.2906|-91.8437
IA|011|ARX|Allamakee|IA011|Allamakee|19005|C|ne|43.2843|-91.3781
IA|018|ARX|Floyd|IA018|Floyd|19067|C|nc|43.06|-92.789
IA|019|ARX|Chickasaw|IA019|Chickasaw|19037|C|ne|43.0601|-92.3176
IA|029|ARX|Fayette|IA029|Fayette|19065|C|ne|42.8625|-91.8443
IA|030|ARX|Clayton|IA030|Clayton|19043|C|ne|42.8447|-91.3414
MN|079|ARX|Wabasha|MN079|Wabasha|27157|C|se|44.2842|-92.2303
MN|086|ARX|Dodge|MN086|Dodge|27039|C|se|44.0225|-92.862
MN|087|ARX|Olmsted|MN087|Olmsted|27109|C|se|44.0036|-92.4018
MN|088|ARX|Winona|MN088|Winona|27169|C|se|43.9869|-91.7791
MN|094|ARX|Mower|MN094|Mower|27099|C|se|43.6714|-92.7525
MN|095|ARX|Fillmore|MN095|Fillmore|27045|C|se|43.674|-92.0901
MN|096|ARX|Houston|MN096|Houston|27055|C|se|43.6714|-91.4928
WI|017|ARX|Taylor|WI017|Taylor|55119|C|nc|45.2115|-90.5012
WI|029|ARX|Clark|WI029|Clark|55019|C|cc|44.7347|-90.6121
WI|032|ARX|Buffalo|WI032|Buffalo|55011|C|wc|44.3799|-91.7545
WI|033|ARX|Trempealeau|WI033|Trempealeau|55121|C|wc|44.304|-91.3585
WI|034|ARX|Jackson|WI034|Jackson|55053|C|wc|44.3191|-90.8052
WI|041|ARX|La Crosse|WI041|La Crosse|55063|C|wc|43.9065|-91.1152
WI|042|ARX|Monroe|WI042|Monroe|55081|C|wc|43.9457|-90.6179
WI|043|ARX|Juneau|WI043|Juneau|55057|C|cc|43.9245|-90.114
WI|044|ARX|Adams|WI044|Adams|55001|C|cc|43.9696|-89.7706
WI|053|ARX|Vernon|WI053|Vernon|55123|C|sw|43.5939|-90.8344
WI|054|ARX|Crawford|WI054|Crawford|55023|C|sw|43.2395|-90.931
WI|055|ARX|Richland|WI055|Richland|55103|C|sw|43.3756|-90.4295
WI|061|ARX|Grant|WI061|Grant|55043|C|sw|42.8675|-90.7062
NY|009|BGM|Northern Oneida|NY009|Oneida|36065|E|cc|43.3813|-75.4692
NY|015|BGM|Yates|NY015|Yates|36123|E|cc|42.6335|-77.1055
NY|016|BGM|Seneca|NY016|Seneca|36099|E|cc|42.781|-76.8237
NY|017|BGM|Southern Cayuga|NY017|Cayuga|36011|E|cc|42.8012|-76.5302
NY|018|BGM|Onondaga|NY018|Onondaga|36067|E|cc|43.0058|-76.1946
NY|022|BGM|Steuben|NY022|Steuben|36101|E|cc|42.2678|-77.3838
NY|023|BGM|Schuyler|NY023|Schuyler|36097|E|cc|42.3938|-76.8752
NY|024|BGM|Chemung|NY024|Chemung|36015|E|cc|42.1413|-76.76
NY|025|BGM|Tompkins|NY025|Tompkins|36109|E|cc|42.452|-76.4737
NY|036|BGM|Madison|NY036|Madison|36053|E|cc|42.9129|-75.6697
NY|037|BGM|Southern Oneida|NY037|Oneida|36065|E|cc|43.12|-75.4068
NY|044|BGM|Cortland|NY044|Cortland|36023|E|cc|42.595|-76.0702
NY|045|BGM|Chenango|NY045|Chenango|36017|E|cc|42.4936|-75.6115
NY|046|BGM|Otsego|NY046|Otsego|36077|E|cc|42.6338|-75.0326
NY|055|BGM|Tioga|NY055|Tioga|36107|E|cc|42.1703|-76.3063
NY|056|BGM|Broome|NY056|Broome|36007|E|cc|42.1602|-75.8196
NY|057|BGM|Delaware|NY057|Delaware|36025|E|cc|42.1982|-74.9665
NY|062|BGM|Sullivan|NY062|Sullivan|36105|E|cc|41.7164|-74.7681
PA|038|BGM|Bradford|PA038|Bradford|42015|E|ne|41.7886|-76.5157
PA|039|BGM|Susquehanna|PA039|Susquehanna|42115|E|ne|41.8214|-75.8008
PA|040|BGM|Northern Wayne|PA040|Wayne|42127|E|ne|41.7773|-75.2898
PA|043|BGM|Wyoming|PA043|Wyoming|42131|E|ne|41.5184|-76.0165
PA|044|BGM|Lackawanna|PA044|Lackawanna|42069|E|ne|41.437|-75.6092
PA|047|BGM|Luzerne|PA047|Luzerne|42079|E|ne|41.1772|-75.9889
PA|048|BGM|Pike|PA048|Pike|42103|E|ne|41.3321|-75.0337
PA|072|BGM|Southern Wayne|PA072|Wayne|42127|E|ne|41.4763|-75.3213
ND|001|BIS|Divide|ND001|Divide|38023|C|nw|48.8149|-103.4873
ND|002|BIS|Burke|ND002|Burke|38013|C|nw|48.7909|-102.5183
ND|003|BIS|Renville|ND003|Renville|38075|C|nc|48.7192|-101.6581
ND|004|BIS|Bottineau|ND004|Bottineau|38009|C|nc|48.7921|-100.8335
ND|005|BIS|Rolette|ND005|Rolette|38079|C|nc|48.7724|-99.8411
ND|009|BIS|Williams|ND009|Williams|38105|C|nw|48.3437|-103.4802
ND|010|BIS|Mountrail|ND010|Mountrail|38061|C|nw|48.2013|-102.3556
ND|011|BIS|Ward|ND011|Ward|38101|C|nc|48.2218|-101.5418
ND|012|BIS|McHenry|ND012|McHenry|38049|C|nc|48.2346|-100.6363
ND|013|BIS|Pierce|ND013|Pierce|38069|C|nc|48.2496|-99.9718
ND|017|BIS|McKenzie|ND017|McKenzie|38053|CM|nw|47.7402|-103.3953
ND|018|BIS|Dunn|ND018|Dunn|38025|CM|sw|47.3568|-102.6182
ND|019|BIS|Mercer|ND019|Mercer|38057|C|sc|47.3092|-101.8315
ND|020|BIS|Oliver|ND020|Oliver|38065|C|sc|47.1153|-101.3403
ND|021|BIS|McLean|ND021|McLean|38055|C|sc|47.607|-101.3218
ND|022|BIS|Sheridan|ND022|Sheridan|38083|C|sc|47.5754|-100.3456
ND|023|BIS|Wells|ND023|Wells|38103|C|sc|47.5876|-99.661
ND|025|BIS|Foster|ND025|Foster|38031|C|se|47.4571|-98.8831
ND|031|BIS|Golden Valley|ND031|Golden Valley|38033|M|sw|46.9402|-103.8467
ND|032|BIS|Billings|ND032|Billings|38007|M|sw|47.0235|-103.3764
ND|033|BIS|Stark|ND033|Stark|38089|M|sw|46.8107|-102.655
ND|034|BIS|Morton|ND034|Morton|38059|C|sc|46.7161|-101.2811
ND|035|BIS|Burleigh|ND035|Burleigh|38015|C|sc|46.9774|-100.4688
ND|036|BIS|Kidder|ND036|Kidder|38043|C|sc|46.9802|-99.7801
ND|037|BIS|Stutsman|ND037|Stutsman|38093|C|se|46.9792|-98.9588
ND|040|BIS|Slope|ND040|Slope|38087|M|sw|46.4472|-103.4599
ND|041|BIS|Hettinger|ND041|Hettinger|38041|M|sw|46.4326|-102.4604
ND|042|BIS|Grant|ND042|Grant|38037|M|sc|46.3583|-101.6397
ND|043|BIS|Bowman|ND043|Bowman|38011|M|sw|46.1126|-103.5207
ND|044|BIS|Adams|ND044|Adams|38001|M|sw|46.0969|-102.5285
ND|045|BIS|Sioux|ND045|Sioux|38085|CM|sc|46.1126|-101.0405
ND|046|BIS|Emmons|ND046|Emmons|38029|C|sc|46.2851|-100.2388
ND|047|BIS|Logan|ND047|Logan|38047|C|se|46.4574|-99.4775
ND|048|BIS|La Moure|ND048|LaMoure|38045|C|se|46.4569|-98.5355
ND|050|BIS|McIntosh|ND050|McIntosh|38051|C|se|46.1119|-99.4412
ND|051|BIS|Dickey|ND051|Dickey|38021|C|se|46.1102|-98.5046
AL|011|BMX|Marion|AL011|Marion|01093|C|nw|34.1366|-87.8871
AL|012|BMX|Lamar|AL012|Lamar|01075|C|wc|33.7792|-88.0969
AL|013|BMX|Fayette|AL013|Fayette|01057|C|wc|33.7212|-87.7389
AL|014|BMX|Winston|AL014|Winston|01133|C|nw|34.1492|-87.3737
AL|015|BMX|Walker|AL015|Walker|01127|C|c|33.8034|-87.2973
AL|017|BMX|Blount|AL017|Blount|01009|C|c|33.9809|-86.5674
AL|018|BMX|Etowah|AL018|Etowah|01055|C|ne|34.0453|-86.0348
AL|019|BMX|Calhoun|AL019|Calhoun|01015|C|ec|33.7714|-85.8261
AL|020|BMX|Cherokee|AL020|Cherokee|01019|C|ne|34.176|-85.6038
AL|021|BMX|Cleburne|AL021|Cleburne|01029|C|ec|33.6745|-85.5188
AL|022|BMX|Pickens|AL022|Pickens|01107|C|wc|33.2809|-88.0887
AL|023|BMX|Tuscaloosa|AL023|Tuscaloosa|01125|C|wc|33.2895|-87.525
AL|024|BMX|Jefferson|AL024|Jefferson|01073|C|c|33.5543|-86.8965
AL|025|BMX|Shelby|AL025|Shelby|01117|C|c|33.2643|-86.6607
AL|026|BMX|St. Clair|AL026|St. Clair|01115|C|c|33.7157|-86.3147
AL|027|BMX|Talladega|AL027|Talladega|01121|C|ec|33.38|-86.1659
AL|028|BMX|Clay|AL028|Clay|01027|C|ec|33.2691|-85.8605
AL|029|BMX|Randolph|AL029|Randolph|01111|C|ec|33.2938|-85.4591
AL|030|BMX|Sumter|AL030|Sumter|01119|C|wc|32.591|-88.1988
AL|031|BMX|Greene|AL031|Greene|01063|C|wc|32.8531|-87.9522
AL|032|BMX|Hale|AL032|Hale|01065|C|wc|32.7627|-87.6291
AL|033|BMX|Perry|AL033|Perry|01105|C|c|32.6385|-87.2942
AL|034|BMX|Bibb|AL034|Bibb|01007|C|c|32.9986|-87.1264
AL|035|BMX|Chilton|AL035|Chilton|01021|C|c|32.8479|-86.7188
AL|036|BMX|Coosa|AL036|Coosa|01037|C|ec|32.9362|-86.2476
AL|037|BMX|Tallapoosa|AL037|Tallapoosa|01123|C|ec|32.8624|-85.7975
AL|038|BMX|Chambers|AL038|Chambers|01017|C|ec|32.9144|-85.392
AL|039|BMX|Marengo|AL039|Marengo|01091|C|sw|32.2476|-87.7895
AL|040|BMX|Dallas|AL040|Dallas|01047|C|sc|32.3258|-87.1065
AL|041|BMX|Autauga|AL041|Autauga|01001|C|c|32.5349|-86.6428
AL|042|BMX|Lowndes|AL042|Lowndes|01085|C|sc|32.1547|-86.6501
AL|043|BMX|Elmore|AL043|Elmore|01051|C|ec|32.5966|-86.1492
AL|044|BMX|Montgomery|AL044|Montgomery|01101|C|sc|32.2202|-86.2076
AL|045|BMX|Macon|AL045|Macon|01087|C|se|32.386|-85.6926
AL|046|BMX|Bullock|AL046|Bullock|01011|C|se|32.1005|-85.7161
AL|047|BMX|Lee|AL047|Lee|01081|C|ec|32.6012|-85.3556
AL|048|BMX|Russell|AL048|Russell|01113|C|se|32.2884|-85.1849
AL|049|BMX|Pike|AL049|Pike|01109|C|se|31.8024|-85.9409
AL|050|BMX|Barbour|AL050|Barbour|01005|C|se|31.8696|-85.3932
ID|011|BOI|West Central Mountains|ID011|Adams|16003|M|wc|44.7716|-115.8966
ID|011|BOI|West Central Mountains|ID011|Gem|16045|M|sw|44.7716|-115.8966
ID|011|BOI|West Central Mountains|ID011|Valley|16085|M|wc|44.7716|-115.8966
ID|011|BOI|West Central Mountains|ID011|Washington|16087|M|sw|44.7716|-115.8966
ID|012|BOI|Lower Treasure Valley|ID012|Canyon|16027|M|sw|43.7962|-116.692
ID|012|BOI|Lower Treasure Valley|ID012|Gem|16045|M|sw|43.7962|-116.692
ID|012|BOI|Lower Treasure Valley|ID012|Owyhee|16073|M|sw|43.7962|-116.692
ID|012|BOI|Lower Treasure Valley|ID012|Payette|16075|M|sw|43.7962|-116.692
ID|012|BOI|Lower Treasure Valley|ID012|Washington|16087|M|sw|43.7962|-116.692
ID|013|BOI|Boise Mountains|ID013|Boise|16015|M|wc|43.7521|-115.4718
ID|013|BOI|Boise Mountains|ID013|Camas|16025|M|cc|43.7521|-115.4718
ID|013|BOI|Boise Mountains|ID013|Elmore|16039|M|sw|43.7521|-115.4718
ID|014|BOI|Upper Treasure Valley|ID014|Ada|16001|M|sw|43.1035|-115.8643
ID|014|BOI|Upper Treasure Valley|ID014|Elmore|16039|M|sw|43.1035|-115.8643
ID|014|BOI|Upper Treasure Valley|ID014|Owyhee|16073|M|sw|43.1035|-115.8643
ID|015|BOI|Southwest Highlands|ID015|Owyhee|16073|M|sw|42.3439|-116.0477
ID|016|BOI|Western Magic Valley|ID016|Gooding|16047|M|sc|42.7508|-114.5943
ID|016|BOI|Western Magic Valley|ID016|Jerome|16053|M|sc|42.7508|-114.5943
ID|016|BOI|Western Magic Valley|ID016|Twin Falls|16083|M|sc|42.7508|-114.5943
ID|028|BOI|Camas Prairie|ID028|Camas|16025|M|cc|43.301|-114.8183
ID|028|BOI|Camas Prairie|ID028|Elmore|16039|M|sw|43.301|-114.8183
ID|029|BOI|Owyhee Mountains|ID029|Owyhee|16073|M|sw|42.9537|-116.7748
ID|030|BOI|Southern Twin Falls County|ID030|Twin Falls|16083|M|sc|42.2255|-114.6784
ID|033|BOI|Upper Weiser River|ID033|Adams|16003|M|wc|44.476|-116.5799
ID|033|BOI|Upper Weiser River|ID033|Washington|16087|M|sw|44.476|-116.5799
OR|061|BOI|Harney County|OR061|Harney|41025|P|se|43.064|-118.9679
OR|062|BOI|Baker County|OR062|Baker|41001|P|ne|44.7092|-117.6753
OR|063|BOI|Malheur County|OR063|Malheur|41045|MP|se|43.123|-117.6604
OR|064|BOI|Oregon Lower Treasure Valley|OR064|Malheur|41045|MP|se|44.0233|-117.1835
CO|030|BOU|Jackson County Below 9000 Feet|CO030|Jackson|08057|M|nc|40.6766|-106.309
CO|031|BOU|West Jackson and West Grand Counties Above 9000 Feet|CO031|Grand|08049|M|nc|40.6175|-106.6092
CO|031|BOU|West Jackson and West Grand Counties Above 9000 Feet|CO031|Jackson|08057|M|nc|40.6175|-106.6092
CO|032|BOU|Grand and Summit Counties Below 9000 Feet|CO032|Grand|08049|M|nc|40.0726|-106.209
CO|032|BOU|Grand and Summit Counties Below 9000 Feet|CO032|Summit|08117|M|cc|40.0726|-106.209
CO|033|BOU|South and East Jackson/Larimer/North and Northeast Grand/Northwest Boulder Counties Above 9000 Feet|CO033|Boulder|08013|M|ne|40.488|-105.9071
CO|033|BOU|South and East Jackson/Larimer/North and Northeast Grand/Northwest Boulder Counties Above 9000 Feet|CO033|Grand|08049|M|nc|40.488|-105.9071
CO|033|BOU|South and East Jackson/Larimer/North and Northeast Grand/Northwest Boulder Counties Above 9000 Feet|CO033|Jackson|08057|M|nc|40.488|-105.9071
CO|033|BOU|South and East Jackson/Larimer/North and Northeast Grand/Northwest Boulder Counties Above 9000 Feet|CO033|Larimer|08069|M|nc|40.488|-105.9071
CO|034|BOU|South and Southeast Grand/West Central and Southwest Boulder/Gilpin/Clear Creek/Summit/North and West Park Counties Above 9000 Feet|CO034|Boulder|08013|M|ne|39.6044|-105.8505
CO|034|BOU|South and Southeast Grand/West Central and Southwest Boulder/Gilpin/Clear Creek/Summit/North and West Park Counties Above 9000 Feet|CO034|Clear Creek|08019|M|cc|39.6044|-105.8505
CO|034|BOU|South and Southeast Grand/West Central and Southwest Boulder/Gilpin/Clear Creek/Summit/North and West Park Counties Above 9000 Feet|CO034|Gilpin|08047|M|cc|39.6044|-105.8505
CO|034|BOU|South and Southeast Grand/West Central and Southwest Boulder/Gilpin/Clear Creek/Summit/North and West Park Counties Above 9000 Feet|CO034|Grand|08049|M|nc|39.6044|-105.8505
CO|034|BOU|South and Southeast Grand/West Central and Southwest Boulder/Gilpin/Clear Creek/Summit/North and West Park Counties Above 9000 Feet|CO034|Jefferson|08059|M|ne|39.6044|-105.8505
CO|034|BOU|South and Southeast Grand/West Central and Southwest Boulder/Gilpin/Clear Creek/Summit/North and West Park Counties Above 9000 Feet|CO034|Park|08093|M|cc|39.6044|-105.8505
CO|034|BOU|South and Southeast Grand/West Central and Southwest Boulder/Gilpin/Clear Creek/Summit/North and West Park Counties Above 9000 Feet|CO034|Summit|08117|M|cc|39.6044|-105.8505
CO|035|BOU|Larimer and Boulder Counties Between 6000 and 9000 Feet|CO035|Boulder|08013|M|ne|40.6099|-105.4708
CO|035|BOU|Larimer and Boulder Counties Between 6000 and 9000 Feet|CO035|Larimer|08069|M|nc|40.6099|-105.4708
CO|036|BOU|Jefferson and West Douglas Counties Above  6000 Feet/Gilpin/Clear Creek/Northeast Park Counties Below 9000 Feet|CO036|Clear Creek|08019|M|cc|39.4838|-105.2681
CO|036|BOU|Jefferson and West Douglas Counties Above  6000 Feet/Gilpin/Clear Creek/Northeast Park Counties Below 9000 Feet|CO036|Douglas|08035|M|ne|39.4838|-105.2681
CO|036|BOU|Jefferson and West Douglas Counties Above  6000 Feet/Gilpin/Clear Creek/Northeast Park Counties Below 9000 Feet|CO036|Gilpin|08047|M|cc|39.4838|-105.2681
CO|036|BOU|Jefferson and West Douglas Counties Above  6000 Feet/Gilpin/Clear Creek/Northeast Park Counties Below 9000 Feet|CO036|Jefferson|08059|M|ne|39.4838|-105.2681
CO|036|BOU|Jefferson and West Douglas Counties Above  6000 Feet/Gilpin/Clear Creek/Northeast Park Counties Below 9000 Feet|CO036|Park|08093|M|cc|39.4838|-105.2681
CO|037|BOU|Central and Southeast Park County|CO037|Park|08093|M|cc|38.9846|-105.6737
CO|038|BOU|Larimer County Below 6000 Feet/Northwest Weld County|CO038|Larimer|08069|M|nc|40.7183|-104.8423
CO|038|BOU|Larimer County Below 6000 Feet/Northwest Weld County|CO038|Weld|08123|M|ne|40.7183|-104.8423
CO|039|BOU|Boulder And Jefferson Counties Below 6000 Feet/West Broomfield County|CO039|Boulder|08013|M|ne|39.9606|-105.156
CO|039|BOU|Boulder And Jefferson Counties Below 6000 Feet/West Broomfield County|CO039|Broomfield|08014|M|ne|39.9606|-105.156
CO|039|BOU|Boulder And Jefferson Counties Below 6000 Feet/West Broomfield County|CO039|Jefferson|08059|M|ne|39.9606|-105.156
CO|040|BOU|North Douglas County Below 6000 Feet/Denver/West Adams and Arapahoe Counties/East Broomfield County|CO040|Adams|08001|M|ne|39.7656|-104.804
CO|040|BOU|North Douglas County Below 6000 Feet/Denver/West Adams and Arapahoe Counties/East Broomfield County|CO040|Arapahoe|08005|M|ne|39.7656|-104.804
CO|040|BOU|North Douglas County Below 6000 Feet/Denver/West Adams and Arapahoe Counties/East Broomfield County|CO040|Broomfield|08014|M|ne|39.7656|-104.804
CO|040|BOU|North Douglas County Below 6000 Feet/Denver/West Adams and Arapahoe Counties/East Broomfield County|CO040|Denver|08031|M|ne|39.7656|-104.804
CO|040|BOU|North Douglas County Below 6000 Feet/Denver/West Adams and Arapahoe Counties/East Broomfield County|CO040|Douglas|08035|M|ne|39.7656|-104.804
CO|041|BOU|Elbert/Central and East Douglas Counties Above 6000 Feet|CO041|Arapahoe|08005|M|ne|39.3075|-104.5091
CO|041|BOU|Elbert/Central and East Douglas Counties Above 6000 Feet|CO041|Douglas|08035|M|ne|39.3075|-104.5091
CO|041|BOU|Elbert/Central and East Douglas Counties Above 6000 Feet|CO041|Elbert|08039|M|ec|39.3075|-104.5091
CO|042|BOU|Northeast Weld County|CO042|Weld|08123|M|ne|40.7427|-104.0025
CO|043|BOU|Central and South Weld County|CO043|Weld|08123|M|ne|40.2668|-104.5924
CO|044|BOU|Morgan County|CO044|Morgan|08087|M|ne|40.2627|-103.8098
CO|045|BOU|Central and East Adams and Arapahoe Counties|CO045|Adams|08001|M|ne|39.7839|-104.1048
CO|045|BOU|Central and East Adams and Arapahoe Counties|CO045|Arapahoe|08005|M|ne|39.7839|-104.1048
CO|046|BOU|North and Northeast Elbert County Below 6000 Feet/North Lincoln County|CO046|Elbert|08039|M|ec|39.356|-103.6814
CO|046|BOU|North and Northeast Elbert County Below 6000 Feet/North Lincoln County|CO046|Lincoln|08073|M|ec|39.356|-103.6814
CO|047|BOU|Southeast Elbert County Below 6000 Feet/South Lincoln County|CO047|Elbert|08039|M|ec|38.8048|-103.5944
CO|047|BOU|Southeast Elbert County Below 6000 Feet/South Lincoln County|CO047|Lincoln|08073|M|ec|38.8048|-103.5944
CO|048|BOU|Logan County|CO048|Logan|08075|M|ne|40.7247|-103.1101
CO|049|BOU|Washington County|CO049|Washington|08121|M|ne|39.971|-103.2013
CO|050|BOU|Sedgwick County|CO050|Sedgwick|08115|M|ne|40.8758|-102.3518
CO|051|BOU|Phillips County|CO051|Phillips|08095|M|ne|40.5939|-102.3575
CT|002|BOX|Hartford|CT002|Hartford|09003|E|nn|41.8064|-72.7328
CT|003|BOX|Tolland|CT003|Tolland|09013|E|nn|41.855|-72.3365
CT|004|BOX|Windham|CT004|Windham|09015|E|nn|41.83|-71.9875
MA|002|BOX|Western Franklin|MA002|Franklin|25011|E|ww|42.6171|-72.7907
MA|003|BOX|Eastern Franklin|MA003|Franklin|25011|E|ww|42.5591|-72.4514
MA|004|BOX|Northern Worcester|MA004|Worcester|25027|E|cc|42.4539|-71.9778
MA|005|BOX|Central Middlesex County|MA005|Middlesex|25017|E|se|42.4633|-71.3797
MA|006|BOX|Western Essex|MA006|Essex|25009|E|ee|42.7153|-71.0659
MA|007|BOX|Eastern Essex|MA007|Essex|25009|E|ee|42.6372|-70.8674
MA|008|BOX|Western Hampshire|MA008|Hampshire|25015|E|ww|42.3891|-72.8687
MA|009|BOX|Western Hampden|MA009|Hampden|25013|E|ww|42.1675|-72.9334
MA|010|BOX|Eastern Hampshire|MA010|Hampshire|25015|E|ww|42.3044|-72.5146
MA|011|BOX|Eastern Hampden|MA011|Hampden|25013|E|ww|42.1202|-72.493
MA|012|BOX|Southern Worcester|MA012|Worcester|25027|E|cc|42.1513|-71.7709
MA|013|BOX|Western Norfolk|MA013|Norfolk|25021|E|ee|42.1423|-71.2658
MA|014|BOX|Southeast Middlesex|MA014|Middlesex|25017|E|se|42.4193|-71.157
MA|015|BOX|Suffolk|MA015|Norfolk|25021|E|ee|42.3308|-71.0826
MA|015|BOX|Suffolk|MA015|Suffolk|25025|E|ee|42.3308|-71.0826
MA|016|BOX|Eastern Norfolk|MA016|Norfolk|25021|E|ee|42.2217|-71.0093
MA|017|BOX|Northern Bristol|MA017|Bristol|25005|E|se|41.9171|-71.1849
MA|018|BOX|Western Plymouth|MA018|Plymouth|25023|E|se|41.9679|-70.8932
MA|019|BOX|Eastern Plymouth|MA019|Norfolk|25021|E|ee|42.0271|-70.7171
MA|019|BOX|Eastern Plymouth|MA019|Plymouth|25023|E|se|42.0271|-70.7171
MA|020|BOX|Southern Bristol|MA020|Bristol|25005|E|se|41.6746|-71.0384
MA|021|BOX|Southern Plymouth|MA021|Plymouth|25023|E|se|41.7415|-70.7761
MA|022|BOX|Barnstable|MA022|Barnstable|25001|E|se|41.7262|-70.2986
MA|023|BOX|Dukes|MA023|Dukes|25007|E|se|41.3966|-70.6561
MA|024|BOX|Nantucket|MA024|Nantucket|25019|E|se|41.2781|-70.0744
MA|026|BOX|Northwest Middlesex County|MA026|Middlesex|25017|E|se|42.6386|-71.6598
NH|011|BOX|Cheshire|NH011|Cheshire|33005|E|ss|42.9193|-72.2512
NH|012|BOX|Eastern Hillsborough|NH012|Hillsborough|33011|E|ss|42.8448|-71.4574
NH|015|BOX|Western And Central Hillsborough|NH015|Hillsborough|33011|E|ss|42.9363|-71.7929
RI|001|BOX|Northwest Providence|RI001|Providence|44007|E||41.8908|-71.6203
RI|002|BOX|Southeast Providence|RI002|Providence|44007|E||41.8121|-71.4526
RI|003|BOX|Western Kent|RI003|Kent|44003|E||41.6644|-71.6637
RI|004|BOX|Eastern Kent|RI004|Kent|44003|E||41.6861|-71.4647
RI|005|BOX|Bristol|RI005|Bristol|44001|E||41.7161|-71.2842
RI|006|BOX|Washington|RI006|Washington|44009|E||41.478|-71.6248
RI|007|BOX|Newport|RI007|Newport|44005|E||41.556|-71.2366
RI|008|BOX|Block Island|RI008|Washington|44009|E||41.178|-71.5785
TX|248|BRO|Zapata|TX248|Zapata|48505|C|sc|27.0008|-99.1686
TX|249|BRO|Jim Hogg|TX249|Jim Hogg|48247|C|sc|27.0434|-98.6973
TX|250|BRO|Brooks|TX250|Brooks|48047|C|sc|27.0316|-98.2187
TX|251|BRO|Inland Kenedy|TX251|Kenedy|48261|C|sc|26.9205|-97.7793
TX|252|BRO|Starr|TX252|Starr|48427|C|sc|26.5621|-98.7384
TX|253|BRO|Southern Hidalgo|TX253|Hidalgo|48215|C|sc|26.2769|-98.1789
TX|254|BRO|Inland Willacy|TX254|Willacy|48489|C|sc|26.4665|-97.7187
TX|255|BRO|Inland Cameron|TX255|Cameron|48061|C|sc|26.1202|-97.5793
TX|351|BRO|Coastal Kenedy|TX351|Kenedy|48261|C|sc|26.9556|-97.4956
TX|353|BRO|Northern Hidalgo |TX353|Hidalgo|48215|C|sc|26.6133|-98.1849
TX|354|BRO|Coastal Willacy|TX354|Willacy|48489|C|sc|26.4868|-97.4673
TX|355|BRO|Coastal Cameron|TX355|Cameron|48061|C|sc|26.17|-97.3264
TX|451|BRO|Kenedy Island|TX451|Kenedy|48261|C|sc|26.9012|-97.3609
TX|454|BRO|Willacy Island|TX454|Willacy|48489|C|sc|26.5229|-97.2769
TX|455|BRO|Cameron Island|TX455|Cameron|48061|C|sc|26.1485|-97.1763
NY|026|BTV|Northern St. Lawrence|NY026|St. Lawrence|36089|E|nn|44.8467|-74.9154
NY|027|BTV|Northern Franklin|NY027|Franklin|36033|E|nn|44.9016|-74.4258
NY|028|BTV|Eastern Clinton|NY028|Clinton|36019|E|nn|44.8026|-73.5131
NY|029|BTV|Southeastern St. Lawrence|NY029|St. Lawrence|36089|E|nn|44.3207|-74.8555
NY|030|BTV|Southern Franklin|NY030|Franklin|36033|E|nn|44.5162|-74.2734
NY|031|BTV|Western Clinton|NY031|Clinton|36019|E|nn|44.7069|-73.7931
NY|034|BTV|Western Essex|NY034|Essex|36031|E|nn|44.0851|-73.8551
NY|035|BTV|Eastern Essex|NY035|Essex|36031|E|nn|44.2489|-73.4345
NY|087|BTV|Southwestern St. Lawrence|NY087|St. Lawrence|36089|E|nn|44.5173|-75.3061
VT|001|BTV|Grand Isle|VT001|Grand Isle|50013|E|nw|44.7968|-73.2948
VT|002|BTV|Western Franklin|VT002|Franklin|50011|E|nw|44.8517|-73.034
VT|003|BTV|Orleans|VT003|Orleans|50019|E|ne|44.8288|-72.2438
VT|004|BTV|Essex|VT004|Essex|50009|E|nn|44.7281|-71.7364
VT|005|BTV|Western Chittenden|VT005|Chittenden|50007|E|nw|44.4793|-73.1562
VT|006|BTV|Lamoille|VT006|Lamoille|50015|E|nw|44.6057|-72.6414
VT|007|BTV|Caledonia|VT007|Caledonia|50005|E|ne|44.4647|-72.1022
VT|008|BTV|Washington|VT008|Washington|50023|E|cc|44.2734|-72.6149
VT|009|BTV|Western Addison|VT009|Addison|50001|E|cc|44.0215|-73.2394
VT|010|BTV|Orange|VT010|Orange|50017|E|cc|44.0056|-72.3769
VT|011|BTV|Western Rutland|VT011|Rutland|50021|E|ss|43.5856|-73.1398
VT|016|BTV|Eastern Franklin|VT016|Franklin|50011|E|nw|44.8662|-72.7255
VT|017|BTV|Eastern Chittenden|VT017|Chittenden|50007|E|nw|44.4237|-72.9287
VT|018|BTV|Eastern Addison|VT018|Addison|50001|E|cc|44.0466|-72.9674
VT|019|BTV|Eastern Rutland|VT019|Rutland|50021|E|ss|43.5713|-72.8735
VT|020|BTV|Western Windsor|VT020|Windsor|50027|E|ss|43.6473|-72.7043
VT|021|BTV|Eastern Windsor|VT021|Windsor|50027|E|ss|43.5254|-72.4895
NY|001|BUF|Niagara|NY001|Niagara|36063|E|ww|43.2011|-78.7425
NY|002|BUF|Orleans|NY002|Orleans|36073|E|ww|43.2522|-78.2312
NY|003|BUF|Monroe|NY003|Monroe|36055|E|ww|43.1464|-77.6959
NY|004|BUF|Wayne|NY004|Wayne|36117|E|ww|43.1566|-77.0292
NY|005|BUF|Northern Cayuga|NY005|Cayuga|36011|E|cc|43.1775|-76.6084
NY|006|BUF|Oswego|NY006|Oswego|36075|E|cc|43.426|-76.1412
NY|007|BUF|Jefferson|NY007|Jefferson|36045|E|cc|44.0409|-75.9102
NY|008|BUF|Lewis|NY008|Lewis|36049|E|cc|43.7847|-75.4488
NY|010|BUF|Northern Erie|NY010|Erie|36029|E|ww|42.9375|-78.6923
NY|011|BUF|Genesee|NY011|Genesee|36037|E|ww|43.001|-78.1936
NY|012|BUF|Wyoming|NY012|Wyoming|36121|E|ww|42.7023|-78.2245
NY|013|BUF|Livingston|NY013|Livingston|36051|E|ww|42.7281|-77.7754
NY|014|BUF|Ontario|NY014|Ontario|36069|E|ww|42.8529|-77.2998
NY|019|BUF|Chautauqua|NY019|Chautauqua|36013|E|ww|42.2282|-79.3664
NY|020|BUF|Cattaraugus|NY020|Cattaraugus|36009|E|ww|42.2486|-78.6789
NY|021|BUF|Allegany|NY021|Allegany|36003|E|ww|42.2574|-78.0276
NY|085|BUF|Southern Erie|NY085|Erie|36029|E|ww|42.6247|-78.7608
MT|029|BYZ|Musselshell|MT029|Musselshell|30065|M|cc|46.4966|-108.3977
MT|030|BYZ|Treasure|MT030|Treasure|30103|M|se|46.2115|-107.2717
MT|031|BYZ|Northern Rosebud|MT031|Rosebud|30087|M|se|46.3849|-106.7762
MT|032|BYZ|Custer|MT032|Custer|30017|M|se|46.2527|-105.5718
MT|033|BYZ|Fallon|MT033|Fallon|30025|M|se|46.334|-104.4174
MT|034|BYZ|Northern Stillwater|MT034|Stillwater|30095|M|sc|45.8098|-109.2176
MT|036|BYZ|Powder River|MT036|Powder River|30075|M|se|45.395|-105.6301
MT|037|BYZ|Carter|MT037|Carter|30011|M|se|45.5168|-104.5362
MT|040|BYZ|Northern Park|MT040|Park|30067|M|sc|45.9621|-110.6013
MT|042|BYZ|Golden Valley|MT042|Golden Valley|30037|M|cc|46.3251|-109.1643
MT|056|BYZ|Red Lodge Foothills|MT056|Carbon|30009|M|M|45.2833|-109.2924
MT|057|BYZ|Northern Big Horn|MT057|Big Horn|30003|M|sc|45.7318|-107.4595
MT|058|BYZ|Southern Rosebud|MT058|Rosebud|30087|M|se|45.4286|-106.4963
MT|063|BYZ|Judith Gap|MT063|Golden Valley|30037|M|cc|46.6384|-109.6782
MT|063|BYZ|Judith Gap|MT063|Wheatland|30107|M|cc|46.6384|-109.6782
MT|064|BYZ|Paradise Valley|MT064|Park|30067|M|sc|45.3939|-110.7098
MT|065|BYZ|Livingston Area|MT065|Park|30067|M|sc|45.6959|-110.5011
MT|066|BYZ|Beartooth Foothills|MT066|Stillwater|30095|M|sc|45.5734|-109.8035
MT|066|BYZ|Beartooth Foothills|MT066|Sweet Grass|30097|M|sc|45.5734|-109.8035
MT|067|BYZ|Absaroka/Beartooth Mountains|MT067|Carbon|30009|M|M|45.2637|-110.1893
MT|067|BYZ|Absaroka/Beartooth Mountains|MT067|Park|30067|M|sc|45.2637|-110.1893
MT|067|BYZ|Absaroka/Beartooth Mountains|MT067|Stillwater|30095|M|sc|45.2637|-110.1893
MT|067|BYZ|Absaroka/Beartooth Mountains|MT067|Sweet Grass|30097|M|sc|45.2637|-110.1893
MT|068|BYZ|Crazy Mountains|MT068|Park|30067|M|sc|46.0653|-110.3156
MT|068|BYZ|Crazy Mountains|MT068|Sweet Grass|30097|M|sc|46.0653|-110.3156
MT|068|BYZ|Crazy Mountains|MT068|Wheatland|30107|M|cc|46.0653|-110.3156
MT|138|BYZ|Southern Big Horn|MT138|Big Horn|30003|M|sc|45.2712|-107.3455
MT|139|BYZ|Southeastern Carbon|MT139|Big Horn|30003|M|sc|45.1361|-108.8466
MT|139|BYZ|Southeastern Carbon|MT139|Carbon|30009|M|sc|45.1361|-108.8466
MT|141|BYZ|Northern Sweet Grass|MT141|Sweet Grass|30097|M|sc|45.9146|-109.8014
MT|169|BYZ|Bighorn Canyon|MT169|Big Horn|30003|M|sc|45.1827|-108.1417
MT|169|BYZ|Bighorn Canyon|MT169|Carbon|30009|M|sc|45.1827|-108.1417
MT|170|BYZ|Northern Carbon|MT170|Carbon|30009|M|sc|45.4565|-108.9346
MT|171|BYZ|Pryor/Northern Bighorn Mountains|MT171|Big Horn|30003|M|sc|45.1683|-108.2446
MT|171|BYZ|Pryor/Northern Bighorn Mountains|MT171|Carbon|30009|M|sc|45.1683|-108.2446
MT|172|BYZ|Melville Foothills|MT172|Sweet Grass|30097|M|sc|46.1376|-110.0264
MT|172|BYZ|Melville Foothills|MT172|Wheatland|30107|M|sc|46.1376|-110.0264
MT|173|BYZ|Northeastern Yellowstone|MT173|Yellowstone|30111|M|sc|46.1581|-107.9135
MT|228|BYZ|Southern Wheatland|MT228|Wheatland|30107|M|sc|46.4003|-109.8006
MT|235|BYZ|Southwestern Yellowstone|MT235|Yellowstone|30111|M|sc|45.8003|-108.4981
WY|198|BYZ|Northeast Big Horn Mountains|WY098|Sheridan|56033|M|nc|44.7706|-107.492
WY|199|BYZ|Sheridan Foothills|WY099|Sheridan|56033|M|nc|44.7977|-106.6544
GA|040|CAE|Lincoln|GA040|Lincoln|13181|E|ec|33.7936|-82.4512
GA|063|CAE|McDuffie|GA063|McDuffie|13189|E|ec|33.4829|-82.4814
GA|064|CAE|Columbia|GA064|Columbia|13073|E|ec|33.5442|-82.264
GA|065|CAE|Richmond|GA065|Richmond|13245|E|ec|33.3596|-82.0735
GA|077|CAE|Burke|GA077|Burke|13033|E|ec|33.0612|-82.0008
SC|016|CAE|Chesterfield|SC016|Chesterfield|45025|E|cc|34.6397|-80.1586
SC|018|CAE|McCormick|SC018|McCormick|45065|E|cc|33.8996|-82.3099
SC|020|CAE|Newberry|SC020|Newberry|45071|E|cc|34.2898|-81.6001
SC|021|CAE|Fairfield|SC021|Fairfield|45039|E|cc|34.3951|-81.1212
SC|022|CAE|Kershaw|SC022|Kershaw|45055|E|cc|34.3388|-80.5903
SC|025|CAE|Edgefield|SC025|Edgefield|45037|E|cc|33.7723|-81.9666
SC|026|CAE|Saluda|SC026|Saluda|45081|E|cc|34.0061|-81.7269
SC|027|CAE|Lexington|SC027|Lexington|45063|E|cc|33.9022|-81.2722
SC|028|CAE|Richland|SC028|Richland|45079|E|cc|34.0218|-80.9031
SC|029|CAE|Lee|SC029|Lee|45061|E|cc|34.1633|-80.2545
SC|030|CAE|Aiken|SC030|Aiken|45003|E|cc|33.5444|-81.6348
SC|031|CAE|Sumter|SC031|Sumter|45085|E|cc|33.9162|-80.3823
SC|035|CAE|Barnwell|SC035|Barnwell|45011|E|cc|33.2661|-81.435
SC|037|CAE|Calhoun|SC037|Calhoun|45017|E|cc|33.6749|-80.7802
SC|038|CAE|Clarendon|SC038|Clarendon|45027|E|cc|33.6658|-80.2164
SC|041|CAE|Bamberg|SC041|Bamberg|45009|E|cc|33.2147|-81.0542
SC|115|CAE|Northern Lancaster |SC115|Lancaster|45057|E|cc|34.9326|-80.842
SC|116|CAE|Southern Lancaster |SC116|Lancaster|45057|E|cc|34.6577|-80.6893
SC|135|CAE|Northwestern Orangeburg|SC135|Orangeburg|45075|E|cc|33.5756|-81.1333
SC|136|CAE|Central Orangeburg|SC136|Orangeburg|45075|E|cc|33.4489|-80.9111
SC|137|CAE|Southeastern Orangeburg|SC137|Orangeburg|45075|E|cc|33.3649|-80.5375
ME|001|CAR|Northwest Aroostook|ME001|Aroostook|23003|E|nn|46.948|-69.1077
ME|002|CAR|Northeast Aroostook|ME002|Aroostook|23003|E|nn|46.7264|-68.2182
ME|003|CAR|Northern Somerset|ME003|Somerset|23025|E|wc|46.2366|-69.9716
ME|004|CAR|Northern Piscataquis|ME004|Piscataquis|23021|E|nc|46.1825|-69.24
ME|005|CAR|Northern Penobscot|ME005|Penobscot|23019|E|ec|45.9454|-68.6456
ME|006|CAR|Southeast Aroostook|ME006|Aroostook|23003|E|nn|46.0031|-68.1173
ME|010|CAR|Central Piscataquis|ME010|Piscataquis|23021|E|nc|45.5609|-69.4281
ME|011|CAR|Central Penobscot|ME011|Penobscot|23019|E|ec|45.3901|-68.4069
ME|015|CAR|Southern Penobscot|ME015|Penobscot|23019|E|ec|44.9362|-68.8441
ME|016|CAR|Interior Hancock|ME016|Hancock|23009|E|se|44.851|-68.3239
ME|017|CAR|Central Washington|ME017|Washington|23029|E|se|45.0093|-67.6338
ME|029|CAR|Coastal Hancock|ME029|Hancock|23009|E|se|44.4349|-68.3928
ME|030|CAR|Coastal Washington|ME030|Washington|23029|E|se|44.6796|-67.5411
ME|031|CAR|Southern Piscataquis|ME031|Piscataquis|23021|E|nc|45.2475|-69.1568
ME|032|CAR|Northern Washington|ME032|Washington|23029|E|se|45.4766|-67.7419
GA|087|CHS|Jenkins|GA087|Jenkins|13165|E|se|32.7925|-81.9636
GA|088|CHS|Screven|GA088|Screven|13251|E|se|32.7507|-81.6119
GA|099|CHS|Candler|GA099|Candler|13043|E|se|32.4035|-82.0737
GA|100|CHS|Bulloch|GA100|Bulloch|13031|E|se|32.3969|-81.7432
GA|101|CHS|Effingham|GA101|Effingham|13103|E|se|32.3675|-81.3407
GA|114|CHS|Tattnall|GA114|Tattnall|13267|E|se|32.0458|-82.0582
GA|115|CHS|Evans|GA115|Evans|13109|E|se|32.1568|-81.8869
GA|116|CHS|Inland Bryan|GA116|Bryan|13029|E|se|32.0404|-81.475
GA|117|CHS|Coastal Bryan|GA117|Bryan|13029|E|se|31.8127|-81.2002
GA|118|CHS|Inland Chatham|GA118|Chatham|13051|E|se|32.0772|-81.2278
GA|119|CHS|Coastal Chatham|GA119|Chatham|13051|E|se|31.9182|-81.0342
GA|119|CHS|Coastal Chatham|GA119|Chatham|13051|E|se|31.9392|-81.0501
GA|137|CHS|Long|GA137|Long|13183|E|se|31.7528|-81.746
GA|138|CHS|Inland Liberty|GA138|Liberty|13179|E|se|31.8508|-81.5352
GA|139|CHS|Coastal Liberty|GA139|Liberty|13179|E|se|31.6625|-81.2029
GA|139|CHS|Coastal Liberty|GA139|Liberty|13179|E|se|31.6716|-81.2012
GA|140|CHS|Inland McIntosh|GA140|McIntosh|13191|E|se|31.5278|-81.4877
GA|141|CHS|Coastal McIntosh|GA141|McIntosh|13191|E|se|31.4585|-81.3001
GA|141|CHS|Coastal McIntosh|GA141|McIntosh|13191|E|se|31.4659|-81.3213
SC|040|CHS|Allendale|SC040|Allendale|45005|E|se|32.9881|-81.3581
SC|042|CHS|Hampton|SC042|Hampton|45049|E|se|32.7763|-81.1406
SC|043|CHS|Inland Colleton|SC043|Colleton|45029|E|se|32.9179|-80.7029
SC|044|CHS|Dorchester|SC044|Dorchester|45035|E|se|33.0795|-80.4052
SC|045|CHS|Inland Berkeley|SC045|Berkeley|45015|E|se|33.222|-79.9542
SC|047|CHS|Inland Jasper|SC047|Jasper|45053|E|se|32.4763|-81.0517
SC|048|CHS|Beaufort|SC048|Beaufort|45013|E|se|32.3568|-80.6933
SC|048|CHS|Beaufort|SC048|Beaufort|45013|E|se|32.3874|-80.7373
SC|049|CHS|Coastal Colleton|SC049|Colleton|45029|E|se|32.6103|-80.498
SC|050|CHS|Charleston|SC050|Charleston|45019|E|se|32.8411|-79.9437
SC|051|CHS|Coastal Jasper|SC051|Jasper|45053|E|se|32.2423|-80.9561
SC|052|CHS|Tidal Berkeley|SC052|Berkeley|45015|E|se|32.9612|-79.9183
OH|003|CLE|Lucas|OH003|Lucas|39095|E|nw|41.62|-83.6586
OH|006|CLE|Wood|OH006|Wood|39173|E|nw|41.3617|-83.623
OH|007|CLE|Ottawa|OH007|Ottawa|39123|E|nw|41.5381|-83.1467
OH|008|CLE|Sandusky|OH008|Sandusky|39143|E|nw|41.3565|-83.145
OH|009|CLE|Erie|OH009|Erie|39043|E|nc|41.3635|-82.6178
OH|010|CLE|Lorain|OH010|Lorain|39093|E|nc|41.2955|-82.1512
OH|011|CLE|Cuyahoga|OH011|Cuyahoga|39035|E|ne|41.4243|-81.6587
OH|012|CLE|Lake|OH012|Lake|39085|E|ne|41.6968|-81.237
OH|013|CLE|Geauga|OH013|Geauga|39055|E|ne|41.4995|-81.1786
OH|014|CLE|Ashtabula Inland|OH014|Ashtabula|39007|E|ne|41.6796|-80.743
OH|017|CLE|Hancock|OH017|Hancock|39063|E|nw|41.0019|-83.6665
OH|018|CLE|Seneca|OH018|Seneca|39147|E|nw|41.1239|-83.1277
OH|019|CLE|Huron|OH019|Huron|39077|E|nc|41.1462|-82.5984
OH|020|CLE|Medina|OH020|Medina|39103|E|ne|41.1176|-81.8997
OH|021|CLE|Summit|OH021|Summit|39153|E|ne|41.1259|-81.5321
OH|022|CLE|Portage|OH022|Portage|39133|E|ne|41.1676|-81.1962
OH|023|CLE|Trumbull|OH023|Trumbull|39155|E|ne|41.3174|-80.7604
OH|027|CLE|Wyandot|OH027|Wyandot|39175|E|nw|40.8424|-83.3044
OH|028|CLE|Crawford|OH028|Crawford|39033|E|nc|40.8509|-82.9197
OH|029|CLE|Richland|OH029|Richland|39139|E|nc|40.7747|-82.5365
OH|030|CLE|Ashland|OH030|Ashland|39005|E|nc|40.8461|-82.2707
OH|031|CLE|Wayne|OH031|Wayne|39169|E|ne|40.8289|-81.8883
OH|032|CLE|Stark|OH032|Stark|39151|E|ne|40.8138|-81.3659
OH|033|CLE|Mahoning|OH033|Mahoning|39099|E|ne|41.0146|-80.7753
OH|036|CLE|Marion|OH036|Marion|39101|E|nc|40.5873|-83.1609
OH|037|CLE|Morrow|OH037|Morrow|39117|E|nc|40.524|-82.7941
OH|038|CLE|Holmes|OH038|Holmes|39075|E|ne|40.5612|-81.9294
OH|047|CLE|Knox|OH047|Knox|39083|E|nc|40.3988|-82.4216
OH|089|CLE|Ashtabula Lakeshore|OH089|Ashtabula|39007|E|ne|41.8761|-80.7817
PA|001|CLE|Northern Erie|PA001|Erie|42049|E|nw|42.1018|-80.1245
PA|002|CLE|Southern Erie|PA002|Erie|42049|E|nw|41.97|-80.014
PA|003|CLE|Crawford|PA003|Crawford|42039|E|nw|41.6848|-80.1063
TX|229|CRP|La Salle|TX229|La Salle|48283|C|sc|28.3451|-99.0997
TX|230|CRP|McMullen|TX230|McMullen|48311|C|sc|28.3491|-98.5675
TX|231|CRP|Live Oak|TX231|Live Oak|48297|C|sc|28.3514|-98.1248
TX|232|CRP|Bee|TX232|Bee|48025|C|sc|28.4174|-97.7412
TX|233|CRP|Goliad|TX233|Goliad|48175|C|sc|28.6571|-97.4264
TX|234|CRP|Victoria|TX234|Victoria|48469|C|se|28.7964|-96.9714
TX|239|CRP|Webb|TX239|Webb|48479|C|sc|27.7611|-99.3316
TX|240|CRP|Duval|TX240|Duval|48131|C|sc|27.6813|-98.5089
TX|241|CRP|Jim Wells|TX241|Jim Wells|48249|C|sc|27.731|-98.0902
TX|242|CRP|Inland Kleberg|TX242|Kleberg|48273|C|sc|27.4319|-97.8503
TX|243|CRP|Inland Nueces|TX243|Nueces|48355|C|sc|27.7423|-97.7226
TX|244|CRP|Inland San Patricio|TX244|San Patricio|48409|C|sc|28.0275|-97.5879
TX|245|CRP|Aransas|TX245|Aransas|48007|C|sc|28.1558|-97.0065
TX|246|CRP|Inland Refugio|TX246|Refugio|48391|C|so|28.3407|-97.208
TX|247|CRP|Inland Calhoun|TX247|Calhoun|48057|C|sc|28.5677|-96.7923
TX|342|CRP|Coastal Kleberg|TX342|Kleberg|48273|C|sc|27.4408|-97.4768
TX|343|CRP|Coastal Nueces|TX343|Nueces|48355|C|sc|27.6637|-97.4107
TX|344|CRP|Coastal San Patricio|TX344|San Patricio|48409|C|sc|27.9431|-97.2647
TX|345|CRP|Aransas County Islands|TX345|Aransas|48007|C|sc|28.0051|-96.9391
TX|346|CRP|Coastal Refugio|TX346|Refugio|48391|C|so|28.2777|-97.0145
TX|347|CRP|Coastal Calhoun|TX347|Calhoun|48057|C|sc|28.5117|-96.5835
TX|442|CRP|Kleberg County Island|TX442|Kleberg|48273|C|sc|27.4267|-97.3101
TX|443|CRP|Nueces County Islands|TX443|Nueces|48355|C|sc|27.7078|-97.1651
TX|447|CRP|Calhoun County Island|TX447|Calhoun|48057|C|sc|28.2324|-96.6387
PA|004|CTP|Warren|PA004|Warren|42123|E|nc|41.8147|-79.2741
PA|005|CTP|McKean|PA005|McKean|42083|E|nc|41.8078|-78.569
PA|006|CTP|Potter|PA006|Potter|42105|E|nc|41.745|-77.8958
PA|010|CTP|Elk|PA010|Elk|42047|E|nc|41.4253|-78.6492
PA|011|CTP|Cameron|PA011|Cameron|42023|E|nc|41.4368|-78.2038
PA|012|CTP|Northern Clinton|PA012|Clinton|42035|E|nc|41.2914|-77.7332
PA|017|CTP|Clearfield|PA017|Clearfield|42033|E|cc|41.0002|-78.4741
PA|018|CTP|Northern Centre|PA018|Centre|42027|E|cc|40.9895|-78.0032
PA|019|CTP|Southern Centre|PA019|Centre|42027|E|cc|40.8739|-77.7022
PA|024|CTP|Cambria|PA024|Cambria|42021|E|cc|40.4954|-78.7136
PA|025|CTP|Blair|PA025|Blair|42013|E|cc|40.4813|-78.3486
PA|026|CTP|Huntingdon|PA026|Huntingdon|42061|E|cc|40.417|-77.9812
PA|027|CTP|Mifflin|PA027|Mifflin|42087|E|cc|40.6104|-77.6171
PA|028|CTP|Juniata|PA028|Juniata|42067|E|cc|40.5311|-77.402
PA|033|CTP|Somerset|PA033|Somerset|42111|E|sc|39.9725|-79.0283
PA|034|CTP|Bedford|PA034|Bedford|42009|E|sc|40.0066|-78.4902
PA|035|CTP|Fulton|PA035|Fulton|42057|E|sc|39.9255|-78.1124
PA|036|CTP|Franklin|PA036|Franklin|42055|E|sc|39.9275|-77.7212
PA|037|CTP|Tioga|PA037|Tioga|42117|E|nc|41.7721|-77.2543
PA|041|CTP|Northern Lycoming|PA041|Lycoming|42081|E|nc|41.4265|-77.1724
PA|042|CTP|Sullivan|PA042|Sullivan|42113|E|nc|41.446|-76.5119
PA|045|CTP|Southern Clinton|PA045|Clinton|42035|E|nc|41.0789|-77.3821
PA|046|CTP|Southern Lycoming|PA046|Lycoming|42081|E|nc|41.2287|-76.9158
PA|049|CTP|Union|PA049|Union|42119|E|cc|40.963|-77.0621
PA|050|CTP|Snyder|PA050|Snyder|42109|E|cc|40.77|-77.0701
PA|051|CTP|Montour|PA051|Montour|42093|E|cc|41.028|-76.6586
PA|052|CTP|Northumberland|PA052|Northumberland|42097|E|cc|40.852|-76.7091
PA|053|CTP|Columbia|PA053|Columbia|42037|E|cc|41.0486|-76.4052
PA|056|CTP|Perry|PA056|Perry|42099|E|sc|40.3984|-77.2622
PA|057|CTP|Dauphin|PA057|Dauphin|42043|E|sc|40.4155|-76.7792
PA|058|CTP|Schuylkill|PA058|Schuylkill|42107|E|cc|40.7059|-76.216
PA|059|CTP|Lebanon|PA059|Lebanon|42075|E|sc|40.3672|-76.4577
PA|063|CTP|Cumberland|PA063|Cumberland|42041|E|sc|40.1637|-77.2651
PA|064|CTP|Adams|PA064|Adams|42001|E|sc|39.8715|-77.2179
PA|065|CTP|York|PA065|York|42133|E|sc|39.9199|-76.7265
PA|066|CTP|Lancaster|PA066|Lancaster|42071|E|sc|40.0424|-76.2477
NE|002|CYS|Dawes|NE002|Dawes|31045|M|pa|42.7197|-103.1354
NE|003|CYS|Box Butte|NE003|Box Butte|31013|M|pa|42.2198|-103.0857
NE|019|CYS|Scotts Bluff|NE019|Scotts Bluff|31157|M|pa|41.8506|-103.708
NE|020|CYS|Banner|NE020|Banner|31007|M|pa|41.546|-103.7104
NE|021|CYS|Morrill|NE021|Morrill|31123|M|pa|41.716|-103.0105
NE|054|CYS|Kimball|NE054|Kimball|31105|M|pa|41.1977|-103.715
NE|055|CYS|Cheyenne|NE055|Cheyenne|31033|M|pa|41.2198|-102.995
NE|095|CYS|North Sioux|NE095|Sioux|31165|M|pa|42.7142|-103.7719
NE|096|CYS|South Sioux|NE096|Sioux|31165|M|pa|42.2153|-103.7432
WY|101|CYS|Converse County Lower Elevations|WY101|Converse|56009|M|ec|43.074|-105.4593
WY|102|CYS|Niobrara County|WY102|Niobrara|56027|M|ec|43.0565|-104.4754
WY|103|CYS|North Laramie Range|WY103|Albany|56001|M|se|42.3535|-105.6241
WY|103|CYS|North Laramie Range|WY103|Converse|56009|M|ec|42.3535|-105.6241
WY|103|CYS|North Laramie Range|WY103|Platte|56031|M|se|42.3535|-105.6241
WY|104|CYS|Ferris/Seminoe/Shirley Mountains|WY104|Carbon|56007|M|sc|42.2707|-106.878
WY|105|CYS|Shirley Basin|WY105|Albany|56001|M|se|42.134|-106.0943
WY|105|CYS|Shirley Basin|WY105|Carbon|56007|M|sc|42.134|-106.0943
WY|106|CYS|Central Laramie Range and Southwest Platte County|WY106|Albany|56001|M|se|41.8778|-105.2243
WY|106|CYS|Central Laramie Range and Southwest Platte County|WY106|Laramie|56021|M|se|41.8778|-105.2243
WY|106|CYS|Central Laramie Range and Southwest Platte County|WY106|Platte|56031|M|se|41.8778|-105.2243
WY|107|CYS|East Platte County|WY107|Platte|56031|M|se|42.2373|-104.8821
WY|108|CYS|Goshen County|WY108|Goshen|56015|M|se|42.088|-104.3533
WY|109|CYS|Central Carbon County|WY109|Carbon|56007|M|sc|41.8204|-107.103
WY|110|CYS|North Snowy Range Foothills|WY110|Albany|56001|M|se|41.6904|-106.259
WY|110|CYS|North Snowy Range Foothills|WY110|Carbon|56007|M|sc|41.6904|-106.259
WY|111|CYS|Southwest Carbon County|WY111|Carbon|56007|M|sc|41.2862|-107.7097
WY|112|CYS|Sierra Madre Range|WY112|Carbon|56007|M|sc|41.1695|-107.099
WY|113|CYS|Upper North Platte River Basin|WY113|Carbon|56007|M|sc|41.3867|-106.7713
WY|114|CYS|Snowy Range|WY114|Albany|56001|M|se|41.3101|-106.3148
WY|114|CYS|Snowy Range|WY114|Carbon|56007|M|sc|41.3101|-106.3148
WY|115|CYS|Laramie Valley|WY115|Albany|56001|M|se|41.4005|-105.7614
WY|116|CYS|South Laramie Range|WY116|Albany|56001|M|se|41.2851|-105.3769
WY|116|CYS|South Laramie Range|WY116|Laramie|56021|M|se|41.2851|-105.3769
WY|117|CYS|South Laramie Range Foothills|WY117|Albany|56001|M|se|41.3136|-105.0324
WY|117|CYS|South Laramie Range Foothills|WY117|Laramie|56021|M|se|41.3136|-105.0324
WY|118|CYS|Central Laramie County|WY118|Laramie|56021|M|se|41.3277|-104.6546
WY|119|CYS|East Laramie County|WY119|Laramie|56021|M|se|41.2851|-104.2337
KS|030|DDC|Trego|KS030|Trego|20195|C|wc|38.9143|-99.8729
KS|031|DDC|Ellis|KS031|Ellis|20051|C|cc|38.9148|-99.3173
KS|043|DDC|Scott|KS043|Scott|20171|C|wc|38.4822|-100.9069
KS|044|DDC|Lane|KS044|Lane|20101|C|wc|38.4814|-100.4664
KS|045|DDC|Ness|KS045|Ness|20135|C|wc|38.4795|-99.9162
KS|046|DDC|Rush|KS046|Rush|20165|C|cc|38.5233|-99.3092
KS|061|DDC|Hamilton|KS061|Hamilton|20075|M|sw|37.9991|-101.7913
KS|062|DDC|Kearny|KS062|Kearny|20093|C|sw|38.0002|-101.3199
KS|063|DDC|Finney|KS063|Finney|20055|C|sw|38.0444|-100.7369
KS|064|DDC|Hodgeman|KS064|Hodgeman|20083|C|sw|38.0875|-99.8979
KS|065|DDC|Pawnee|KS065|Pawnee|20145|C|sc|38.1814|-99.2368
KS|066|DDC|Stafford|KS066|Stafford|20185|C|sc|38.0311|-98.7175
KS|074|DDC|Stanton|KS074|Stanton|20187|C|sw|37.563|-101.7842
KS|075|DDC|Grant|KS075|Grant|20067|C|sw|37.5622|-101.308
KS|076|DDC|Haskell|KS076|Haskell|20081|C|sw|37.5623|-100.8712
KS|077|DDC|Gray|KS077|Gray|20069|C|sw|37.7382|-100.4378
KS|078|DDC|Ford|KS078|Ford|20057|C|sw|37.6917|-99.8879
KS|079|DDC|Edwards|KS079|Edwards|20047|C|sc|37.8876|-99.312
KS|080|DDC|Kiowa|KS080|Kiowa|20097|C|sc|37.5582|-99.286
KS|081|DDC|Pratt|KS081|Pratt|20151|C|sc|37.6478|-98.7396
KS|084|DDC|Morton|KS084|Morton|20129|C|sw|37.1914|-101.7993
KS|085|DDC|Stevens|KS085|Stevens|20189|C|sw|37.1924|-101.3121
KS|086|DDC|Seward|KS086|Seward|20175|C|sw|37.1933|-100.8513
KS|087|DDC|Meade|KS087|Meade|20119|C|sw|37.2382|-100.3662
KS|088|DDC|Clark|KS088|Clark|20025|C|sw|37.2355|-99.8203
KS|089|DDC|Comanche|KS089|Comanche|20033|C|sc|37.1913|-99.2719
KS|090|DDC|Barber|KS090|Barber|20007|C|sc|37.2289|-98.6848
MN|010|DLH|Koochiching|MN010|Koochiching|27071|C|nc|48.2422|-93.7874
MN|011|DLH|North St. Louis|MN011|St. Louis|27137|C|ne|48.139|-92.5294
MN|012|DLH|Northern Cook/Northern Lake|MN012|Cook|27031|C|ne|47.8238|-91.1981
MN|012|DLH|Northern Cook/Northern Lake|MN012|Lake|27075|C|ne|47.8238|-91.1981
MN|018|DLH|North Itasca|MN018|Itasca|27061|C|nc|47.6644|-93.7298
MN|019|DLH|Central St. Louis|MN019|St. Louis|27137|C|ne|47.4461|-92.4352
MN|020|DLH|Southern Lake/North Shore|MN020|Lake|27075|C|ne|47.282|-91.4479
MN|020|DLH|Southern Lake/North Shore|MN020|St. Louis|27137|C|ne|47.282|-91.4479
MN|021|DLH|Southern Cook/North Shore|MN021|Cook|27031|C|ne|47.8033|-90.4117
MN|025|DLH|North Cass|MN025|Cass|27021|C|nc|47.1039|-94.2344
MN|026|DLH|South Itasca|MN026|Itasca|27061|C|nc|47.2596|-93.4742
MN|033|DLH|South Cass|MN033|Cass|27021|C|nc|46.5646|-94.5522
MN|034|DLH|Crow Wing|MN034|Crow Wing|27035|C|ec|46.4824|-94.0709
MN|035|DLH|Northern Aitkin|MN035|Aitkin|27001|C|ec|46.826|-93.4185
MN|036|DLH|South Aitkin|MN036|Aitkin|27001|C|ec|46.4095|-93.4126
MN|037|DLH|Carlton/South St. Louis|MN037|Carlton|27017|C|ne|46.7516|-92.5801
MN|037|DLH|Carlton/South St. Louis|MN037|St. Louis|27137|C|ne|46.7516|-92.5801
MN|038|DLH|Pine|MN038|Pine|27115|C|ec|46.1208|-92.7414
WI|001|DLH|Douglas|WI001|Douglas|55031|C|nw|46.4309|-91.9147
WI|002|DLH|Bayfield|WI002|Bayfield|55007|C|nw|46.5241|-91.2006
WI|003|DLH|Ashland|WI003|Ashland|55003|C|nw|46.3148|-90.6781
WI|004|DLH|Iron|WI004|Iron|55051|C|nw|46.2623|-90.242
WI|006|DLH|Burnett|WI006|Burnett|55013|C|nw|45.8627|-92.3676
WI|007|DLH|Washburn|WI007|Washburn|55129|C|nw|45.8993|-91.7912
WI|008|DLH|Sawyer|WI008|Sawyer|55113|C|nw|45.88|-91.1447
WI|009|DLH|Price|WI009|Price|55099|C|nc|45.6804|-90.3614
IA|004|DMX|Emmet|IA004|Emmet|19063|C|nw|43.3779|-94.6784
IA|005|DMX|Kossuth|IA005|Kossuth|19109|C|nc|43.2042|-94.2067
IA|006|DMX|Winnebago|IA006|Winnebago|19189|C|nc|43.3775|-93.7342
IA|007|DMX|Worth|IA007|Worth|19195|C|nc|43.3774|-93.2609
IA|015|DMX|Palo Alto|IA015|Palo Alto|19147|C|nw|43.082|-94.6782
IA|016|DMX|Hancock|IA016|Hancock|19081|C|nc|43.0818|-93.7343
IA|017|DMX|Cerro Gordo|IA017|Cerro Gordo|19033|C|nc|43.0816|-93.2608
IA|023|DMX|Pocahontas|IA023|Pocahontas|19151|C|nw|42.7341|-94.6789
IA|024|DMX|Humboldt|IA024|Humboldt|19091|C|nc|42.7764|-94.2073
IA|025|DMX|Wright|IA025|Wright|19197|C|nc|42.7331|-93.7352
IA|026|DMX|Franklin|IA026|Franklin|19069|C|nc|42.7325|-93.2624
IA|027|DMX|Butler|IA027|Butler|19023|C|nc|42.7316|-92.7902
IA|028|DMX|Bremer|IA028|Bremer|19017|C|ne|42.7747|-92.3182
IA|033|DMX|Sac|IA033|Sac|19161|C|wc|42.3862|-95.1055
IA|034|DMX|Calhoun|IA034|Calhoun|19025|C|wc|42.3852|-94.6405
IA|035|DMX|Webster|IA035|Webster|19187|C|cc|42.4278|-94.1818
IA|036|DMX|Hamilton|IA036|Hamilton|19079|C|cc|42.3837|-93.7068
IA|037|DMX|Hardin|IA037|Hardin|19083|C|cc|42.3838|-93.2404
IA|038|DMX|Grundy|IA038|Grundy|19075|C|cc|42.4019|-92.791
IA|039|DMX|Black Hawk|IA039|Black Hawk|19013|C|ne|42.4701|-92.3085
IA|044|DMX|Crawford|IA044|Crawford|19047|C|wc|42.0372|-95.3821
IA|045|DMX|Carroll|IA045|Carroll|19027|C|wc|42.0362|-94.8607
IA|046|DMX|Greene|IA046|Greene|19073|C|wc|42.0362|-94.3969
IA|047|DMX|Boone|IA047|Boone|19015|C|cc|42.0366|-93.9318
IA|048|DMX|Story|IA048|Story|19169|C|cc|42.0362|-93.4651
IA|049|DMX|Marshall|IA049|Marshall|19127|C|cc|42.0358|-92.9988
IA|050|DMX|Tama|IA050|Tama|19171|C|cc|42.0798|-92.5326
IA|057|DMX|Audubon|IA057|Audubon|19009|C|wc|41.6846|-94.9058
IA|058|DMX|Guthrie|IA058|Guthrie|19077|C|wc|41.6838|-94.501
IA|059|DMX|Dallas|IA059|Dallas|19049|C|cc|41.6849|-94.0398
IA|060|DMX|Polk|IA060|Polk|19153|C|cc|41.6855|-93.5734
IA|061|DMX|Jasper|IA061|Jasper|19099|C|cc|41.686|-93.0537
IA|062|DMX|Poweshiek|IA062|Poweshiek|19157|C|cc|41.6864|-92.5314
IA|070|DMX|Cass|IA070|Cass|19029|C|sw|41.3315|-94.9278
IA|071|DMX|Adair|IA071|Adair|19001|C|sw|41.3307|-94.471
IA|072|DMX|Madison|IA072|Madison|19121|C|sc|41.3307|-94.0155
IA|073|DMX|Warren|IA073|Warren|19181|C|sc|41.3343|-93.5614
IA|074|DMX|Marion|IA074|Marion|19125|C|sc|41.3344|-93.0995
IA|075|DMX|Mahaska|IA075|Mahaska|19123|C|sc|41.3351|-92.6409
IA|081|DMX|Adams|IA081|Adams|19003|C|sw|41.029|-94.6992
IA|082|DMX|Union|IA082|Union|19175|C|sc|41.0277|-94.2424
IA|083|DMX|Clarke|IA083|Clarke|19039|C|sc|41.029|-93.7851
IA|084|DMX|Lucas|IA084|Lucas|19117|C|sc|41.0293|-93.3277
IA|085|DMX|Monroe|IA085|Monroe|19135|C|sc|41.0297|-92.869
IA|086|DMX|Wapello|IA086|Wapello|19179|C|se|41.0306|-92.4095
IA|092|DMX|Taylor|IA092|Taylor|19173|C|sw|40.7374|-94.6965
IA|093|DMX|Ringgold|IA093|Ringgold|19159|C|sc|40.7352|-94.244
IA|094|DMX|Decatur|IA094|Decatur|19053|C|sc|40.7377|-93.7863
IA|095|DMX|Wayne|IA095|Wayne|19185|C|sc|40.7395|-93.3274
IA|096|DMX|Appanoose|IA096|Appanoose|19007|C|sc|40.7432|-92.8687
IA|097|DMX|Davis|IA097|Davis|19051|C|se|40.7477|-92.4097
MI|047|DTX|Midland|MI047|Midland|26111|E|se|43.6468|-84.3879
MI|048|DTX|Bay|MI048|Bay|26017|E|se|43.7072|-83.9921
MI|049|DTX|Huron|MI049|Huron|26063|E|se|43.8333|-83.0193
MI|053|DTX|Saginaw|MI053|Saginaw|26145|E|se|43.335|-84.0532
MI|054|DTX|Tuscola|MI054|Tuscola|26157|E|se|43.4641|-83.4167
MI|055|DTX|Sanilac|MI055|Sanilac|26151|E|se|43.4235|-82.8201
MI|060|DTX|Shiawassee|MI060|Shiawassee|26155|E|se|42.9537|-84.1467
MI|061|DTX|Genesee|MI061|Genesee|26049|E|se|43.0217|-83.7067
MI|062|DTX|Lapeer|MI062|Lapeer|26087|E|se|43.0901|-83.2218
MI|063|DTX|St. Clair|MI063|St. Clair|26147|E|se|42.9425|-82.682
MI|068|DTX|Livingston|MI068|Livingston|26093|E|se|42.603|-83.9115
MI|069|DTX|Oakland|MI069|Oakland|26125|E|se|42.6604|-83.3855
MI|070|DTX|Macomb|MI070|Macomb|26099|E|se|42.6956|-82.9322
MI|075|DTX|Washtenaw|MI075|Washtenaw|26161|E|se|42.2534|-83.8385
MI|076|DTX|Wayne|MI076|Wayne|26163|E|se|42.284|-83.2865
MI|082|DTX|Lenawee|MI082|Lenawee|26091|E|se|41.8951|-84.0664
MI|083|DTX|Monroe|MI083|Monroe|26115|E|se|41.9292|-83.5373
IA|040|DVN|Buchanan|IA040|Buchanan|19019|C|ne|42.4707|-91.8379
IA|041|DVN|Delaware|IA041|Delaware|19055|C|ne|42.4711|-91.3673
IA|042|DVN|Dubuque|IA042|Dubuque|19061|C|ne|42.4688|-90.8824
IA|051|DVN|Benton|IA051|Benton|19011|C|ec|42.0801|-92.0657
IA|052|DVN|Linn|IA052|Linn|19113|C|ec|42.0789|-91.5989
IA|053|DVN|Jones|IA053|Jones|19105|C|ec|42.1212|-91.1314
IA|054|DVN|Jackson|IA054|Jackson|19097|C|ec|42.1717|-90.5742
IA|063|DVN|Iowa|IA063|Iowa|19095|C|ec|41.6863|-92.0656
IA|064|DVN|Johnson|IA064|Johnson|19103|C|ec|41.6715|-91.5881
IA|065|DVN|Cedar|IA065|Cedar|19031|C|ec|41.7723|-91.1324
IA|066|DVN|Clinton|IA066|Clinton|19045|C|ec|41.898|-90.532
IA|067|DVN|Muscatine|IA067|Muscatine|19139|C|ec|41.4839|-91.1127
IA|068|DVN|Scott|IA068|Scott|19163|C|ec|41.6371|-90.6232
IA|076|DVN|Keokuk|IA076|Keokuk|19107|C|se|41.3364|-92.1787
IA|077|DVN|Washington|IA077|Washington|19183|C|se|41.3356|-91.7179
IA|078|DVN|Louisa|IA078|Louisa|19115|C|se|41.2185|-91.2597
IA|087|DVN|Jefferson|IA087|Jefferson|19101|C|se|41.0318|-91.9489
IA|088|DVN|Henry|IA088|Henry|19087|C|se|40.9879|-91.5446
IA|089|DVN|Des Moines|IA089|Des Moines|19057|C|se|40.9232|-91.1815
IA|098|DVN|Van Buren|IA098|Van Buren|19177|C|se|40.7532|-91.95
IA|099|DVN|Lee|IA099|Lee|19111|C|se|40.642|-91.4792
IL|001|DVN|Jo Daviess|IL001|Jo Daviess|17085|C|nw|42.3657|-90.2123
IL|002|DVN|Stephenson|IL002|Stephenson|17177|C|nw|42.3517|-89.6625
IL|007|DVN|Carroll|IL007|Carroll|17015|C|nw|42.0688|-89.9345
IL|009|DVN|Whiteside|IL009|Whiteside|17195|C|nw|41.7563|-89.9141
IL|015|DVN|Rock Island|IL015|Rock Island|17161|C|nw|41.4674|-90.5674
IL|016|DVN|Henry|IL016|Henry|17073|C|nw|41.3531|-90.1314
IL|017|DVN|Bureau|IL017|Bureau|17011|C|nc|41.4041|-89.5287
IL|018|DVN|Putnam|IL018|Putnam|17155|C|nc|41.2045|-89.2858
IL|024|DVN|Mercer|IL024|Mercer|17131|C|nw|41.2053|-90.7414
IL|025|DVN|Henderson|IL025|Henderson|17071|C|wc|40.8181|-90.9251
IL|026|DVN|Warren|IL026|Warren|17187|C|wc|40.8488|-90.615
IL|034|DVN|Hancock|IL034|Hancock|17067|C|wc|40.4037|-91.1647
IL|035|DVN|McDonough|IL035|McDonough|17109|C|wc|40.4562|-90.678
MO|009|DVN|Scotland|MO009|Scotland|29199|C|ne|40.4526|-92.1471
MO|010|DVN|Clark|MO010|Clark|29045|C|ne|40.4103|-91.7384
KS|025|EAX|Atchison|KS025|Atchison|20005|C|ne|39.532|-95.3129
KS|057|EAX|Miami|KS057|Miami|20121|C|ec|38.5636|-94.8381
KS|060|EAX|Linn|KS060|Linn|20107|C|ec|38.2123|-94.8429
KS|102|EAX|Doniphan|KS102|Doniphan|20043|C|ne|39.7885|-95.147
KS|103|EAX|Leavenworth|KS103|Leavenworth|20103|C|ne|39.1993|-95.0379
KS|104|EAX|Wyandotte|KS104|Wyandotte|20209|C|ne|39.1145|-94.7646
KS|105|EAX|Johnson|KS105|Johnson|20091|C|ec|38.8838|-94.8223
MO|001|EAX|Atchison|MO001|Atchison|29005|C|nw|40.4307|-95.427
MO|002|EAX|Nodaway|MO002|Nodaway|29147|C|nw|40.3607|-94.8834
MO|003|EAX|Worth|MO003|Worth|29227|C|nw|40.4791|-94.4222
MO|004|EAX|Gentry|MO004|Gentry|29075|C|nw|40.2121|-94.4099
MO|005|EAX|Harrison|MO005|Harrison|29081|C|nc|40.3547|-93.9921
MO|006|EAX|Mercer|MO006|Mercer|29129|C|nc|40.4223|-93.5685
MO|007|EAX|Putnam|MO007|Putnam|29171|C|nc|40.4789|-93.0161
MO|008|EAX|Schuyler|MO008|Schuyler|29197|C|ne|40.4702|-92.5209
MO|011|EAX|Holt|MO011|Holt|29087|C|nw|40.0946|-95.215
MO|012|EAX|Andrew|MO012|Andrew|29003|C|nw|39.9834|-94.802
MO|013|EAX|De Kalb|MO013|DeKalb|29063|C|nw|39.8932|-94.4047
MO|014|EAX|Daviess|MO014|Daviess|29061|C|nc|39.9607|-93.9855
MO|015|EAX|Grundy|MO015|Grundy|29079|C|nc|40.114|-93.5653
MO|016|EAX|Sullivan|MO016|Sullivan|29211|C|nc|40.2107|-93.1115
MO|017|EAX|Adair|MO017|Adair|29001|C|ne|40.1906|-92.6007
MO|020|EAX|Buchanan|MO020|Buchanan|29021|C|nw|39.6598|-94.8062
MO|021|EAX|Clinton|MO021|Clinton|29049|C|nw|39.6018|-94.4046
MO|022|EAX|Caldwell|MO022|Caldwell|29025|C|nc|39.6557|-93.9828
MO|023|EAX|Livingston|MO023|Livingston|29117|C|nc|39.7821|-93.5483
MO|024|EAX|Linn|MO024|Linn|29115|C|nc|39.8702|-93.1072
MO|025|EAX|Macon|MO025|Macon|29121|C|nc|39.8308|-92.5646
MO|028|EAX|Platte|MO028|Platte|29165|C|wc|39.3804|-94.7736
MO|029|EAX|Clay|MO029|Clay|29047|C|wc|39.3105|-94.4208
MO|030|EAX|Ray|MO030|Ray|29177|C|wc|39.3524|-93.9899
MO|031|EAX|Carroll|MO031|Carroll|29033|C|nc|39.4268|-93.5051
MO|032|EAX|Chariton|MO032|Chariton|29041|C|nc|39.5145|-92.9626
MO|033|EAX|Randolph|MO033|Randolph|29175|C|nc|39.4402|-92.4971
MO|037|EAX|Jackson|MO037|Jackson|29095|C|wc|39.0085|-94.3461
MO|038|EAX|Lafayette|MO038|Lafayette|29107|C|wc|39.0656|-93.7855
MO|039|EAX|Saline|MO039|Saline|29195|C|cc|39.1366|-93.2022
MO|040|EAX|Howard|MO040|Howard|29089|C|cc|39.1427|-92.6958
MO|043|EAX|Cass|MO043|Cass|29037|C|wc|38.647|-94.3548
MO|044|EAX|Johnson|MO044|Johnson|29101|C|wc|38.7441|-93.8063
MO|045|EAX|Pettis|MO045|Pettis|29159|C|cc|38.7283|-93.2851
MO|046|EAX|Cooper|MO046|Cooper|29053|C|cc|38.8439|-92.8103
MO|053|EAX|Bates|MO053|Bates|29013|C|wc|38.2573|-94.34
MO|054|EAX|Henry|MO054|Henry|29083|C|wc|38.3852|-93.7927
CA|101|EKA|Coastal Del Norte|CA101|Del Norte|06015|P|nw|41.0243|-124.0956
CA|102|EKA|Del Norte Interior|CA102|Del Norte|06015|P|nw|41.0243|-124.0956
CA|103|EKA|Northern Humboldt Coast|CA103|Humboldt|06023|P|nw|41.0243|-124.0956
CA|104|EKA|Southwestern Humboldt|CA104|Humboldt|06023|P|nw|41.0243|-124.0956
CA|105|EKA|Northern Humboldt Interior|CA105|Humboldt|06023|P|nw|41.0243|-124.0956
CA|106|EKA|Southern Humboldt Interior|CA106|Humboldt|06023|P|nw|41.0243|-124.0956
CA|107|EKA|Northern Trinity|CA107|Trinity|06105|P|nw|40.7088|-123.111
CA|108|EKA|Southern Trinity|CA108|Trinity|06105|P|nw|40.7088|-123.111
CA|109|EKA|Mendocino Coast|CA109|Mendocino|06045|P|nw|39.3778|-123.7271
CA|110|EKA|Northwestern Mendocino Interior|CA110|Mendocino|06045|P|nw|39.6359|-123.4371
CA|111|EKA|Northeastern Mendocino Interior|CA111|Mendocino|06045|P|nw|39.7603|-123.1396
CA|112|EKA|Southwestern Mendocino Interior|CA112|Mendocino|06045|P|nw|39.1561|-123.4915
CA|113|EKA|Southeastern Mendocino Interior|CA113|Mendocino|06045|P|nw|39.0904|-123.1953
CA|114|EKA|Northern Lake County|CA114|Lake|06033|P|cc|39.3619|-122.8628
CA|115|EKA|Southern Lake County|CA115|Lake|06033|P|cc|38.9779|-122.7022
NM|401|EPZ|Upper Gila River Valley|NM401|Grant|35017|M|sw|33.0652|-109.0457
NM|401|EPZ|Upper Gila River Valley|NM401|Hidalgo|35023|M|sw|33.0652|-109.0457
NM|403|EPZ|Southern Gila Foothills/Mimbres Valley|NM403|Grant|35017|M|sw|32.5961|-108.0435
NM|403|EPZ|Southern Gila Foothills/Mimbres Valley|NM403|Luna|35029|M|sw|32.5961|-108.0435
NM|404|EPZ|Southwest Desert/Lower Gila River Valley|NM404|Grant|35017|M|sw|32.984|-109.0449
NM|404|EPZ|Southwest Desert/Lower Gila River Valley|NM404|Hidalgo|35023|M|sw|32.984|-109.0449
NM|405|EPZ|Lowlands of the Bootheel|NM405|Grant|35017|M|sw|31.7623|-108.5699
NM|405|EPZ|Lowlands of the Bootheel|NM405|Hidalgo|35023|M|sw|31.7623|-108.5699
NM|406|EPZ|Uplands of the Bootheel|NM406|Hidalgo|35023|M|sw|31.5516|-108.8399
NM|407|EPZ|Southwest Desert/Mimbres Basin|NM407|Grant|35017|M|sw|32.1585|-107.7431
NM|407|EPZ|Southwest Desert/Mimbres Basin|NM407|Luna|35029|M|sw|32.1585|-107.7431
NM|408|EPZ|Eastern Black Range Foothills|NM408|Grant|35017|M|sw|33.0357|-107.5193
NM|408|EPZ|Eastern Black Range Foothills|NM408|Luna|35029|M|sw|33.0357|-107.5193
NM|408|EPZ|Eastern Black Range Foothills|NM408|Sierra|35051|M|sc|33.0357|-107.5193
NM|409|EPZ|Sierra County Lakes|NM409|Sierra|35051|M|sc|33.1033|-107.0436
NM|410|EPZ|Northern Dona Ana County|NM410|Dona Ana|35013|M|sc|32.6132|-106.9177
NM|411|EPZ|Southern Dona Ana County/Mesilla Valley|NM411|Dona Ana|35013|M|sc|32.1002|-106.9151
NM|414|EPZ|West Slopes Sacramento Mountains Below 7500 Feet|NM414|Otero|35035|M|sc|32.8801|-105.7623
NM|415|EPZ|Sacramento Mountains Above 7500 Feet|NM415|Otero|35035|M|sc|32.9911|-105.6803
NM|416|EPZ|East Slopes Sacramento Mountains Below 7500 Feet|NM416|Otero|35035|M|sc|32.9357|-105.4385
NM|417|EPZ|Otero Mesa|NM417|Otero|35035|M|sc|32.261|-105.4233
NM|425|EPZ|Central Grant County/Silver City Area |NM425|Grant|35017|M|sw|32.76|-108.0997
NM|426|EPZ|Southern Gila Region Highlands/Black Range |NM426|Grant|35017|M|sw|33.0716|-108.0453
NM|426|EPZ|Southern Gila Region Highlands/Black Range |NM426|Sierra|35051|M|sw|33.0716|-108.0453
NM|427|EPZ|West Central Tularosa Basin/White Sands |NM427|Sierra|35051|M|sc|32.7419|-106.4202
NM|427|EPZ|West Central Tularosa Basin/White Sands |NM427|Dona Ana|35013|M|sc|32.7419|-106.4202
NM|427|EPZ|West Central Tularosa Basin/White Sands |NM427|Otero|35035|M|sc|32.7419|-106.4202
NM|428|EPZ|East Central Tularosa Basin/Alamogordo |NM428|Otero|35035|M|sc|33.0694|-106.0993
NM|429|EPZ|Southeast Tularosa Basin |NM429|Otero|35035|M|sc|32.3354|-106.1094
TX|418|EPZ|Western El Paso County|TX418|El Paso|48141|M|sw|31.8933|-106.5545
TX|419|EPZ|Eastern/Central El Paso County|TX419|El Paso|48141|M|sw|31.8096|-106.2948
TX|420|EPZ|Northern Hudspeth Highlands/Hueco Mountains|TX420|El Paso|48141|M|sw|31.7056|-105.7878
TX|420|EPZ|Northern Hudspeth Highlands/Hueco Mountains|TX420|Hudspeth|48229|M|sw|31.7056|-105.7878
TX|421|EPZ|Salt Basin|TX421|Hudspeth|48229|M|sw|31.7396|-105.2179
TX|422|EPZ|Southern Hudspeth Highlands|TX422|Hudspeth|48229|M|sw|31.1872|-105.1931
TX|423|EPZ|Rio Grande Valley of Eastern El Paso/Western Hudspeth Counties|TX423|El Paso|48141|M|sw|31.3635|-105.8909
TX|423|EPZ|Rio Grande Valley of Eastern El Paso/Western Hudspeth Counties|TX423|Hudspeth|48229|M|sw|31.3635|-105.8909
TX|424|EPZ|Rio Grande Valley of Eastern Hudspeth County|TX424|Hudspeth|48229|M|sw|30.8825|-105.2707
TX|171|EWX|Llano|TX171|Llano|48299|C|sc|30.7056|-98.684
TX|172|EWX|Burnet|TX172|Burnet|48053|C|sc|30.7883|-98.1824
TX|173|EWX|Williamson|TX173|Williamson|48491|C|sc|30.6481|-97.6008
TX|183|EWX|Val Verde|TX183|Val Verde|48465|C|sc|29.893|-101.1517
TX|184|EWX|Edwards|TX184|Edwards|48137|C|sc|29.9826|-100.3047
TX|185|EWX|Real|TX185|Real|48385|C|sc|29.8318|-99.8221
TX|186|EWX|Kerr|TX186|Kerr|48265|C|sc|30.0615|-99.3501
TX|187|EWX|Bandera|TX187|Bandera|48019|C|sc|29.7472|-99.2463
TX|188|EWX|Gillespie|TX188|Gillespie|48171|C|sc|30.3181|-98.9464
TX|189|EWX|Kendall|TX189|Kendall|48259|C|sc|29.9447|-98.7116
TX|190|EWX|Blanco|TX190|Blanco|48031|C|sc|30.2664|-98.3998
TX|191|EWX|Hays|TX191|Hays|48209|C|sc|30.0582|-98.0311
TX|192|EWX|Travis|TX192|Travis|48453|C|sc|30.3347|-97.7819
TX|193|EWX|Bastrop|TX193|Bastrop|48021|C|sc|30.1036|-97.3121
TX|194|EWX|Lee|TX194|Lee|48287|C|sc|30.3107|-96.9657
TX|202|EWX|Kinney|TX202|Kinney|48271|C|sc|29.3502|-100.418
TX|203|EWX|Uvalde|TX203|Uvalde|48463|C|sc|29.3573|-99.7622
TX|204|EWX|Medina|TX204|Medina|48325|C|sc|29.3557|-99.1101
TX|205|EWX|Bexar|TX205|Bexar|48029|C|sc|29.4491|-98.5199
TX|206|EWX|Comal|TX206|Comal|48091|C|sc|29.8082|-98.2782
TX|207|EWX|Guadalupe|TX207|Guadalupe|48187|C|sc|29.5831|-97.9484
TX|208|EWX|Caldwell|TX208|Caldwell|48055|C|sc|29.8372|-97.62
TX|209|EWX|Fayette|TX209|Fayette|48149|C|sc|29.8768|-96.9198
TX|217|EWX|Maverick|TX217|Maverick|48323|C|sc|28.7426|-100.3145
TX|218|EWX|Zavala|TX218|Zavala|48507|C|sc|28.8662|-99.7606
TX|219|EWX|Frio|TX219|Frio|48163|C|sc|28.8678|-99.1083
TX|220|EWX|Atascosa|TX220|Atascosa|48013|C|sc|28.8907|-98.5279
TX|221|EWX|Wilson|TX221|Wilson|48493|C|sc|29.1741|-98.0866
TX|222|EWX|Karnes|TX222|Karnes|48255|C|sc|28.9057|-97.8594
TX|223|EWX|Gonzales|TX223|Gonzales|48177|C|sc|29.4567|-97.4925
TX|224|EWX|De Witt|TX224|DeWitt|48123|C|sc|29.0821|-97.3568
TX|225|EWX|Lavaca|TX225|Lavaca|48285|C|sc|29.3843|-96.9302
TX|228|EWX|Dimmit|TX228|Dimmit|48127|C|sc|28.4225|-99.7567
GA|001|FFC|Dade|GA001|Dade|13083|E|nw|34.8546|-85.5045
GA|002|FFC|Walker|GA002|Walker|13295|E|nw|34.7356|-85.3009
GA|003|FFC|Catoosa|GA003|Catoosa|13047|E|nw|34.9036|-85.1381
GA|004|FFC|Whitfield|GA004|Whitfield|13313|E|nw|34.8056|-84.9673
GA|005|FFC|Murray|GA005|Murray|13213|E|nw|34.7885|-84.7481
GA|006|FFC|Fannin|GA006|Fannin|13111|E|nc|34.8641|-84.3197
GA|007|FFC|Gilmer|GA007|Gilmer|13123|E|nc|34.6915|-84.4554
GA|008|FFC|Union|GA008|Union|13291|E|nc|34.8342|-83.9907
GA|009|FFC|Towns|GA009|Towns|13281|E|ne|34.9167|-83.7373
GA|011|FFC|Chattooga|GA011|Chattooga|13055|E|nw|34.475|-85.3454
GA|012|FFC|Gordon|GA012|Gordon|13129|E|nw|34.5034|-84.8757
GA|013|FFC|Pickens|GA013|Pickens|13227|E|nc|34.4643|-84.4656
GA|014|FFC|Dawson|GA014|Dawson|13085|E|nc|34.4438|-84.1704
GA|015|FFC|Lumpkin|GA015|Lumpkin|13187|E|nc|34.5721|-84.0031
GA|016|FFC|White|GA016|White|13311|E|ne|34.6464|-83.7472
GA|019|FFC|Floyd|GA019|Floyd|13115|E|nw|34.2632|-85.2143
GA|020|FFC|Bartow|GA020|Bartow|13015|E|nw|34.2379|-84.8405
GA|021|FFC|Cherokee|GA021|Cherokee|13057|E|nc|34.2439|-84.4764
GA|022|FFC|Forsyth|GA022|Forsyth|13117|E|nc|34.2255|-84.1253
GA|023|FFC|Hall|GA023|Hall|13139|E|nc|34.3168|-83.8197
GA|024|FFC|Banks|GA024|Banks|13011|E|ne|34.3541|-83.4974
GA|025|FFC|Jackson|GA025|Jackson|13157|E|ne|34.1339|-83.5663
GA|027|FFC|Madison|GA027|Madison|13195|E|ne|34.1279|-83.209
GA|030|FFC|Polk|GA030|Polk|13233|E|nw|34.0018|-85.1882
GA|031|FFC|Paulding|GA031|Paulding|13223|E|nw|33.9202|-84.8672
GA|032|FFC|Cobb|GA032|Cobb|13067|E|nc|33.9415|-84.5767
GA|033|FFC|North Fulton|GA033|Fulton|13121|E|nc|33.935|-84.3557
GA|034|FFC|Gwinnett|GA034|Gwinnett|13135|E|nc|33.9617|-84.0235
GA|035|FFC|Barrow|GA035|Barrow|13013|E|nc|33.9932|-83.7127
GA|036|FFC|Clarke|GA036|Clarke|13059|E|ne|33.9513|-83.3674
GA|037|FFC|Oconee|GA037|Oconee|13219|E|ne|33.8349|-83.437
GA|038|FFC|Oglethorpe|GA038|Oglethorpe|13221|E|ne|33.8807|-83.0806
GA|039|FFC|Wilkes|GA039|Wilkes|13317|E|ec|33.782|-82.7432
GA|041|FFC|Haralson|GA041|Haralson|13143|E|nw|33.7942|-85.211
GA|042|FFC|Carroll|GA042|Carroll|13045|E|nw|33.5828|-85.0797
GA|043|FFC|Douglas|GA043|Douglas|13097|E|nc|33.7015|-84.7677
GA|044|FFC|South Fulton|GA044|Fulton|13121|E|nc|33.6085|-84.6065
GA|045|FFC|De Kalb|GA045|DeKalb|13089|E|nc|33.7715|-84.2263
GA|046|FFC|Rockdale|GA046|Rockdale|13247|E|nc|33.6545|-84.0267
GA|047|FFC|Walton|GA047|Walton|13297|E|nc|33.7816|-83.7338
GA|047|FFC|Walton|GA047|Walton|13297|E|nc|33.7816|-83.7338
GA|048|FFC|Newton|GA048|Newton|13217|E|nc|33.5551|-83.8503
GA|049|FFC|Morgan|GA049|Morgan|13211|E|nc|33.5908|-83.4924
GA|050|FFC|Greene|GA050|Greene|13133|E|ec|33.5789|-83.1667
GA|051|FFC|Taliaferro|GA051|Taliaferro|13265|E|ec|33.5662|-82.8787
GA|052|FFC|Heard|GA052|Heard|13149|E|wc|33.297|-85.1283
GA|053|FFC|Coweta|GA053|Coweta|13077|E|wc|33.3535|-84.7633
GA|054|FFC|Fayette|GA054|Fayette|13113|E|nc|33.414|-84.4941
GA|055|FFC|Clayton|GA055|Clayton|13063|E|nc|33.5419|-84.3577
GA|056|FFC|Spalding|GA056|Spalding|13255|E|wc|33.2609|-84.2841
GA|057|FFC|Henry|GA057|Henry|13151|E|nc|33.4534|-84.1554
GA|058|FFC|Butts|GA058|Butts|13035|E|cc|33.2891|-83.9572
GA|059|FFC|Jasper|GA059|Jasper|13159|E|cc|33.3164|-83.6881
GA|060|FFC|Putnam|GA060|Putnam|13237|E|cc|33.3218|-83.3728
GA|061|FFC|Hancock|GA061|Hancock|13141|E|ec|33.2703|-83.001
GA|062|FFC|Warren|GA062|Warren|13301|E|ec|33.4089|-82.6767
GA|066|FFC|Troup|GA066|Troup|13285|E|wc|33.0335|-85.0283
GA|067|FFC|Meriwether|GA067|Meriwether|13199|E|wc|33.0406|-84.6883
GA|068|FFC|Pike|GA068|Pike|13231|E|wc|33.0922|-84.3892
GA|069|FFC|Upson|GA069|Upson|13293|E|wc|32.8813|-84.2993
GA|070|FFC|Lamar|GA070|Lamar|13171|E|wc|33.0765|-84.1394
GA|071|FFC|Monroe|GA071|Monroe|13207|E|cc|33.0141|-83.9187
GA|072|FFC|Jones|GA072|Jones|13169|E|cc|33.0251|-83.5605
GA|073|FFC|Baldwin|GA073|Baldwin|13009|E|cc|33.069|-83.2499
GA|074|FFC|Washington|GA074|Washington|13303|E|ec|32.9695|-82.7959
GA|075|FFC|Glascock|GA075|Glascock|13125|E|ec|33.2293|-82.6107
GA|076|FFC|Jefferson|GA076|Jefferson|13163|E|ec|33.0549|-82.4181
GA|078|FFC|Harris|GA078|Harris|13145|E|wc|32.736|-84.909
GA|079|FFC|Talbot|GA079|Talbot|13263|E|wc|32.6995|-84.533
GA|080|FFC|Taylor|GA080|Taylor|13269|E|wc|32.5556|-84.2504
GA|081|FFC|Crawford|GA081|Crawford|13079|E|cc|32.7145|-83.9864
GA|082|FFC|Bibb|GA082|Bibb|13021|E|cc|32.8067|-83.6979
GA|083|FFC|Twiggs|GA083|Twiggs|13289|E|cc|32.6672|-83.4272
GA|084|FFC|Wilkinson|GA084|Wilkinson|13319|E|cc|32.8024|-83.1713
GA|085|FFC|Johnson|GA085|Johnson|13167|E|ec|32.7015|-82.6601
GA|086|FFC|Emanuel|GA086|Emanuel|13107|E|ec|32.5898|-82.3018
GA|089|FFC|Muscogee|GA089|Muscogee|13215|E|wc|32.51|-84.877
GA|090|FFC|Chattahoochee|GA090|Chattahoochee|13053|E|wc|32.347|-84.787
GA|091|FFC|Marion|GA091|Marion|13197|E|wc|32.3534|-84.5246
GA|092|FFC|Schley|GA092|Schley|13249|E|wc|32.262|-84.3149
GA|093|FFC|Macon|GA093|Macon|13193|E|wc|32.3584|-84.0425
GA|094|FFC|Peach|GA094|Peach|13225|E|cc|32.5688|-83.8269
GA|095|FFC|Houston|GA095|Houston|13153|E|cc|32.459|-83.6662
GA|096|FFC|Bleckley|GA096|Bleckley|13023|E|cc|32.4344|-83.3279
GA|097|FFC|Laurens|GA097|Laurens|13175|E|cc|32.4637|-82.9222
GA|098|FFC|Treutlen|GA098|Treutlen|13283|E|ec|32.4039|-82.5673
GA|102|FFC|Stewart|GA102|Stewart|13259|E|wc|32.0785|-84.8352
GA|103|FFC|Webster|GA103|Webster|13307|E|wc|32.0466|-84.551
GA|104|FFC|Sumter|GA104|Sumter|13261|E|wc|32.04|-84.1971
GA|105|FFC|Dooly|GA105|Dooly|13093|E|cc|32.1572|-83.7987
GA|106|FFC|Crisp|GA106|Crisp|13081|E|cc|31.923|-83.7681
GA|107|FFC|Pulaski|GA107|Pulaski|13235|E|cc|32.2328|-83.4764
GA|108|FFC|Wilcox|GA108|Wilcox|13315|E|cc|31.9733|-83.4322
GA|109|FFC|Dodge|GA109|Dodge|13091|E|cc|32.1722|-83.1684
GA|110|FFC|Telfair|GA110|Telfair|13271|E|cc|31.9298|-82.9389
GA|111|FFC|Wheeler|GA111|Wheeler|13309|E|cc|32.1171|-82.7246
GA|112|FFC|Montgomery|GA112|Montgomery|13209|E|cc|32.1746|-82.5338
GA|113|FFC|Toombs|GA113|Toombs|13279|E|se|32.1206|-82.3306
MN|001|FGF|West Polk|MN001|Polk|27119|C|nw|47.8466|-96.7048
MN|002|FGF|Norman|MN002|Norman|27107|C|nw|47.3265|-96.4551
MN|003|FGF|Clay|MN003|Clay|27027|C|nw|46.8924|-96.4906
MN|004|FGF|Kittson|MN004|Kittson|27069|C|nw|48.7766|-96.7826
MN|005|FGF|Roseau|MN005|Roseau|27135|C|nw|48.7751|-95.8107
MN|006|FGF|Lake Of The Woods|MN006|Lake of the Woods|27077|C|nc|48.7719|-94.9051
MN|007|FGF|West Marshall|MN007|Marshall|27089|C|nw|48.3592|-96.7657
MN|008|FGF|East Marshall|MN008|Marshall|27089|C|nw|48.3571|-95.9961
MN|009|FGF|North Beltrami|MN009|Beltrami|27007|C|nc|48.1627|-95.0124
MN|013|FGF|Pennington|MN013|Pennington|27113|C|nw|48.0662|-96.0367
MN|014|FGF|Red Lake|MN014|Red Lake|27125|C|nw|47.8717|-96.0953
MN|015|FGF|East Polk|MN015|Polk|27119|C|nw|47.6577|-95.918
MN|016|FGF|North Clearwater|MN016|Clearwater|27029|C|nw|47.752|-95.3891
MN|017|FGF|South Beltrami|MN017|Beltrami|27007|C|nc|47.6313|-94.8022
MN|022|FGF|Mahnomen|MN022|Mahnomen|27087|C|nw|47.3252|-95.809
MN|023|FGF|South Clearwater|MN023|Clearwater|27029|C|nw|47.3228|-95.3643
MN|024|FGF|Hubbard|MN024|Hubbard|27057|C|nc|47.1087|-94.9166
MN|027|FGF|West Becker|MN027|Becker|27005|C|nw|46.9358|-95.9229
MN|028|FGF|East Becker|MN028|Becker|27005|C|nw|46.9334|-95.4143
MN|029|FGF|Wilkin|MN029|Wilkin|27167|C|wc|46.357|-96.4684
MN|030|FGF|West Otter Tail|MN030|Otter Tail|27111|C|wc|46.4061|-96.0175
MN|031|FGF|East Otter Tail|MN031|Otter Tail|27111|C|wc|46.4109|-95.4624
MN|032|FGF|Wadena|MN032|Wadena|27159|C|cc|46.5858|-94.9694
MN|040|FGF|Grant|MN040|Grant|27051|C|wc|45.934|-96.0121
ND|006|FGF|Towner|ND006|Towner|38095|C|ne|48.6856|-99.2459
ND|007|FGF|Cavalier|ND007|Cavalier|38019|C|ne|48.7722|-98.465
ND|008|FGF|Pembina|ND008|Pembina|38067|C|ne|48.7672|-97.5517
ND|014|FGF|Benson|ND014|Benson|38005|C|ne|48.0694|-99.3659
ND|015|FGF|Ramsey|ND015|Ramsey|38071|C|ne|48.269|-98.7201
ND|016|FGF|Eastern Walsh County|ND016|Walsh|38099|C|ne|48.3683|-97.4998
ND|024|FGF|Eddy|ND024|Eddy|38027|C|ne|47.7176|-98.9016
ND|026|FGF|Nelson|ND026|Nelson|38063|C|ne|47.9216|-98.1921
ND|027|FGF|Grand Forks|ND027|Grand Forks|38035|C|ne|47.9219|-97.457
ND|028|FGF|Griggs|ND028|Griggs|38039|C|se|47.4572|-98.2371
ND|029|FGF|Steele|ND029|Steele|38091|C|se|47.4562|-97.7247
ND|030|FGF|Traill|ND030|Traill|38097|C|se|47.4542|-97.1615
ND|038|FGF|Barnes|ND038|Barnes|38003|C|se|46.9361|-98.0716
ND|039|FGF|Cass|ND039|Cass|38017|C|se|46.933|-97.2481
ND|049|FGF|Ransom|ND049|Ransom|38073|C|se|46.4561|-97.6575
ND|052|FGF|Sargent|ND052|Sargent|38081|C|se|46.1078|-97.6306
ND|053|FGF|Richland|ND053|Richland|38077|C|se|46.2646|-96.9483
ND|054|FGF|Western Walsh County|ND054|Walsh|38099|C|ne|48.3714|-98.084
AZ|004|FGZ|Kaibab Plateau|AZ004|Coconino|04005|m|nc|36.6514|-112.2018
AZ|005|FGZ|Marble and Glen Canyons|AZ005|Coconino|04005|m|nc|36.7777|-111.6681
AZ|006|FGZ|Grand Canyon Country|AZ006|Coconino|04005|m|nc|36.184|-112.3184
AZ|007|FGZ|Coconino Plateau|AZ007|Coconino|04005|m|nc|35.7341|-112.5569
AZ|008|FGZ|Yavapai County  Mountains|AZ008|Yavapai|04025|m|wc|34.8361|-112.6554
AZ|009|FGZ|Northeast Plateaus and Mesas Hwy 264 Northward|AZ009|Apache|04001|m|ne|36.4046|-110.9711
AZ|009|FGZ|Northeast Plateaus and Mesas Hwy 264 Northward|AZ009|Coconino|04005|m|nc|36.4046|-110.9711
AZ|009|FGZ|Northeast Plateaus and Mesas Hwy 264 Northward|AZ009|Navajo|04017|m|ne|36.4046|-110.9711
AZ|010|FGZ|Chinle Valley|AZ010|Apache|04001|m|ne|36.5404|-109.7068
AZ|010|FGZ|Chinle Valley|AZ010|Navajo|04017|m|ne|36.5404|-109.7068
AZ|011|FGZ|Chuska Mountains and Defiance Plateau|AZ011|Apache|04001|m|ne|35.8693|-109.2344
AZ|012|FGZ|Little Colorado River Valley in Coconino County|AZ012|Coconino|04005|m|nc|35.4788|-111.1876
AZ|012|FGZ|Little Colorado River Valley in Coconino County|AZ012|Navajo|04017|m|ne|35.4788|-111.1876
AZ|013|FGZ|Little Colorado River Valley in Navajo County|AZ013|Navajo|04017|m|ne|34.844|-110.3128
AZ|014|FGZ|Little Colorado River Valley in Apache County|AZ014|Apache|04001|m|ne|34.5768|-109.4198
AZ|015|FGZ|Western Mogollon Rim|AZ015|Coconino|04005|m|nc|35.2296|-111.7689
AZ|016|FGZ|Eastern Mogollon Rim|AZ016|Coconino|04005|m|nc|34.4418|-110.8122
AZ|016|FGZ|Eastern Mogollon Rim|AZ016|Navajo|04017|m|ne|34.4418|-110.8122
AZ|017|FGZ|White Mountains|AZ017|Apache|04001|m|ne|33.9272|-109.6483
AZ|017|FGZ|White Mountains|AZ017|Navajo|04017|m|ne|33.9272|-109.6483
AZ|018|FGZ|Northern Gila County|AZ018|Gila|04007|m|ec|34.0401|-110.9225
AZ|037|FGZ|Yavapai County Valleys and Basins|AZ037|Yavapai|04025|m|wc|34.4302|-112.5126
AZ|038|FGZ|Oak Creek and Sycamore Canyons|AZ038|Coconino|04005|m|nc|34.9117|-111.8796
AZ|038|FGZ|Oak Creek and Sycamore Canyons|AZ038|Yavapai|04025|m|wc|34.9117|-111.8796
AZ|039|FGZ|Black Mesa Area|AZ039|Apache|04001|m|ne|36.355|-110.243
AZ|039|FGZ|Black Mesa Area|AZ039|Coconino|04005|m|nc|36.355|-110.243
AZ|039|FGZ|Black Mesa Area|AZ039|Navajo|04017|m|ne|36.355|-110.243
AZ|040|FGZ|Northeast Plateaus and Mesas South of Hwy 264|AZ040|Apache|04001|m|ne|35.4889|-110.1825
AZ|040|FGZ|Northeast Plateaus and Mesas South of Hwy 264|AZ040|Coconino|04005|m|nc|35.4889|-110.1825
AZ|040|FGZ|Northeast Plateaus and Mesas South of Hwy 264|AZ040|Navajo|04017|m|ne|35.4889|-110.1825
IA|001|FSD|Lyon|IA001|Lyon|19119|C|nw|43.3805|-96.2103
IA|002|FSD|Osceola|IA002|Osceola|19143|C|nw|43.3785|-95.6238
IA|003|FSD|Dickinson|IA003|Dickinson|19059|C|nw|43.3779|-95.151
IA|012|FSD|Sioux|IA012|Sioux|19167|C|nw|43.0826|-96.1779
IA|013|FSD|O'Brien|IA013|O'Brien|19141|C|nw|43.0838|-95.625
IA|014|FSD|Clay|IA014|Clay|19041|C|nw|43.0826|-95.151
IA|020|FSD|Plymouth|IA020|Plymouth|19149|C|nw|42.7378|-96.2142
IA|021|FSD|Cherokee|IA021|Cherokee|19035|C|nw|42.7357|-95.6239
IA|022|FSD|Buena Vista|IA022|Buena Vista|19021|C|nw|42.7355|-95.1513
IA|031|FSD|Woodbury|IA031|Woodbury|19193|C|wc|42.3897|-96.0449
IA|032|FSD|Ida|IA032|Ida|19093|C|wc|42.3868|-95.5136
MN|071|FSD|Lincoln|MN071|Lincoln|27081|C|sw|44.4126|-96.2671
MN|072|FSD|Lyon|MN072|Lyon|27083|C|sw|44.4135|-95.839
MN|080|FSD|Murray|MN080|Murray|27101|C|sw|44.0221|-95.7632
MN|081|FSD|Cottonwood|MN081|Cottonwood|27033|C|sw|44.0071|-95.1812
MN|089|FSD|Nobles|MN089|Nobles|27105|C|sw|43.6742|-95.7534
MN|090|FSD|Jackson|MN090|Jackson|27063|C|sw|43.6741|-95.1541
MN|097|FSD|Pipestone|MN097|Pipestone|27117|C|sw|44.023|-96.2586
MN|098|FSD|Rock|MN098|Rock|27133|C|sw|43.6747|-96.2532
NE|013|FSD|Dixon|NE013|Dixon|31051|C|ne|42.4932|-96.8677
NE|014|FSD|Dakota|NE014|Dakota|31043|C|ne|42.3911|-96.5646
SD|038|FSD|Beadle|SD038|Beadle|46005|C|ec|44.4145|-98.2782
SD|039|FSD|Kingsbury|SD039|Kingsbury|46077|C|ec|44.3696|-97.4915
SD|040|FSD|Brookings|SD040|Brookings|46011|C|ec|44.3697|-96.7905
SD|050|FSD|Gregory|SD050|Gregory|46053|C|sc|43.1924|-99.1856
SD|052|FSD|Jerauld|SD052|Jerauld|46073|C|cc|44.0664|-98.6298
SD|053|FSD|Sanborn|SD053|Sanborn|46111|C|ec|44.0235|-98.0914
SD|054|FSD|Miner|SD054|Miner|46097|C|ec|44.022|-97.6102
SD|055|FSD|Lake|SD055|Lake|46079|C|ec|44.022|-97.1294
SD|056|FSD|Moody|SD056|Moody|46101|C|ec|44.0221|-96.671
SD|057|FSD|Brule|SD057|Brule|46015|C|sc|43.7181|-99.081
SD|058|FSD|Aurora|SD058|Aurora|46003|C|sc|43.7182|-98.5616
SD|059|FSD|Davison|SD059|Davison|46035|C|se|43.675|-98.1461
SD|060|FSD|Hanson|SD060|Hanson|46061|C|se|43.6748|-97.7874
SD|061|FSD|McCook|SD061|McCook|46087|C|se|43.6742|-97.3684
SD|062|FSD|Minnehaha|SD062|Minnehaha|46099|C|se|43.6742|-96.7914
SD|063|FSD|Charles Mix|SD063|Charles Mix|46023|C|sc|43.2079|-98.5879
SD|064|FSD|Douglas|SD064|Douglas|46043|C|sc|43.3871|-98.3662
SD|065|FSD|Hutchinson|SD065|Hutchinson|46067|C|se|43.3348|-97.7546
SD|066|FSD|Turner|SD066|Turner|46125|C|se|43.3108|-97.1488
SD|067|FSD|Lincoln|SD067|Lincoln|46083|C|se|43.2789|-96.7219
SD|068|FSD|Bon Homme|SD068|Bon Homme|46009|C|se|42.9884|-97.8847
SD|069|FSD|Yankton|SD069|Yankton|46135|C|se|43.009|-97.3947
SD|070|FSD|Clay|SD070|Clay|46027|C|se|42.9146|-96.9757
SD|071|FSD|Union|SD071|Union|46127|C|se|42.8324|-96.6561
TX|091|FWD|Montague|TX091|Montague|48337|C|nc|33.6757|-97.7246
TX|092|FWD|Cooke|TX092|Cooke|48097|C|nc|33.6393|-97.2126
TX|093|FWD|Grayson|TX093|Grayson|48181|C|nc|33.6268|-96.6776
TX|094|FWD|Fannin|TX094|Fannin|48147|C|nc|33.5939|-96.1066
TX|095|FWD|Lamar|TX095|Lamar|48277|C|ne|33.6671|-95.5711
TX|100|FWD|Young|TX100|Young|48503|C|nc|33.1767|-98.6878
TX|101|FWD|Jack|TX101|Jack|48237|C|nc|33.2335|-98.1725
TX|102|FWD|Wise|TX102|Wise|48497|C|nc|33.2159|-97.6544
TX|103|FWD|Denton|TX103|Denton|48121|C|nc|33.2043|-97.1171
TX|104|FWD|Collin|TX104|Collin|48085|C|nc|33.1878|-96.5724
TX|105|FWD|Hunt|TX105|Hunt|48231|C|nc|33.1236|-96.0854
TX|106|FWD|Delta|TX106|Delta|48119|C|ne|33.3863|-95.6723
TX|107|FWD|Hopkins|TX107|Hopkins|48223|C|ne|33.1495|-95.564
TX|115|FWD|Stephens|TX115|Stephens|48429|C|nc|32.7359|-98.8362
TX|116|FWD|Palo Pinto|TX116|Palo Pinto|48363|C|nc|32.7532|-98.313
TX|117|FWD|Parker|TX117|Parker|48367|C|nc|32.7776|-97.8051
TX|118|FWD|Tarrant|TX118|Tarrant|48439|C|nc|32.7704|-97.2919
TX|119|FWD|Dallas|TX119|Dallas|48113|C|nc|32.7666|-96.7779
TX|120|FWD|Rockwall|TX120|Rockwall|48397|C|nc|32.8978|-96.4077
TX|121|FWD|Kaufman|TX121|Kaufman|48257|C|nc|32.5996|-96.2879
TX|122|FWD|Van Zandt|TX122|Van Zandt|48467|C|ne|32.5637|-95.8365
TX|123|FWD|Rains|TX123|Rains|48379|C|ne|32.8703|-95.7934
TX|129|FWD|Eastland|TX129|Eastland|48133|C|nc|32.3271|-98.8323
TX|130|FWD|Erath|TX130|Erath|48143|C|nc|32.2363|-98.218
TX|131|FWD|Hood|TX131|Hood|48221|C|nc|32.4299|-97.8323
TX|132|FWD|Somervell|TX132|Somervell|48425|C|nc|32.2223|-97.7744
TX|133|FWD|Johnson|TX133|Johnson|48251|C|nc|32.379|-97.3663
TX|134|FWD|Ellis|TX134|Ellis|48139|C|nc|32.3484|-96.7945
TX|135|FWD|Henderson|TX135|Henderson|48213|C|ne|32.2121|-95.8538
TX|141|FWD|Comanche|TX141|Comanche|48093|C|nc|31.948|-98.5582
TX|142|FWD|Mills|TX142|Mills|48333|C|nc|31.4952|-98.5955
TX|143|FWD|Hamilton|TX143|Hamilton|48193|C|nc|31.7048|-98.1107
TX|144|FWD|Bosque|TX144|Bosque|48035|C|nc|31.9004|-97.6343
TX|145|FWD|Hill|TX145|Hill|48217|C|nc|31.9907|-97.1324
TX|146|FWD|Navarro|TX146|Navarro|48349|C|nc|32.047|-96.4724
TX|147|FWD|Freestone|TX147|Freestone|48161|C|nc|31.7049|-96.149
TX|148|FWD|Anderson|TX148|Anderson|48001|C|ne|31.8134|-95.6525
TX|156|FWD|Lampasas|TX156|Lampasas|48281|C|nc|31.1962|-98.2414
TX|157|FWD|Coryell|TX157|Coryell|48099|C|nc|31.3909|-97.7992
TX|158|FWD|Bell|TX158|Bell|48027|C|nc|31.0377|-97.4782
TX|159|FWD|McLennan|TX159|McLennan|48309|C|nc|31.5524|-97.2018
TX|160|FWD|Falls|TX160|Falls|48145|C|nc|31.2533|-96.9358
TX|161|FWD|Limestone|TX161|Limestone|48293|C|nc|31.5455|-96.5805
TX|162|FWD|Leon|TX162|Leon|48289|C|ne|31.2965|-95.9957
TX|174|FWD|Milam|TX174|Milam|48331|C|sc|30.7863|-96.9769
TX|175|FWD|Robertson|TX175|Robertson|48395|C|sc|31.027|-96.5128
MT|016|GGW|Central and Southeast Phillips|MT016|Phillips|30071|M|ne|48.1191|-107.8379
MT|017|GGW|Central and Southern Valley|MT017|Valley|30105|M|ne|48.1821|-106.6828
MT|018|GGW|Daniels|MT018|Daniels|30019|M|ne|48.7838|-105.5485
MT|019|GGW|Sheridan|MT019|Sheridan|30091|M|ne|48.7212|-104.5046
MT|020|GGW|Western Roosevelt|MT020|Roosevelt|30085|M|ne|48.3139|-105.4045
MT|021|GGW|Petroleum|MT021|Petroleum|30069|M|ne|47.1175|-108.2501
MT|022|GGW|Garfield|MT022|Garfield|30033|M|ne|47.2777|-106.9928
MT|023|GGW|McCone|MT023|McCone|30055|M|ne|47.6452|-105.7953
MT|024|GGW|Richland|MT024|Richland|30083|M|ne|47.7879|-104.5614
MT|025|GGW|Dawson|MT025|Dawson|30021|M|ne|47.2664|-104.8994
MT|026|GGW|Prairie|MT026|Prairie|30079|M|ne|46.8605|-105.3779
MT|027|GGW|Wibaux|MT027|Wibaux|30109|M|ne|46.9653|-104.249
MT|059|GGW|Northern Phillips|MT059|Phillips|30071|M|ne|48.7814|-107.7403
MT|060|GGW|Southwest Phillips|MT060|Phillips|30071|M|ne|47.8159|-108.487
MT|061|GGW|Northern Valley|MT061|Valley|30105|M|ne|48.7789|-106.6331
MT|062|GGW|Eastern Roosevelt|MT062|Roosevelt|30085|M|ne|48.2705|-104.5328
KS|005|GID|Phillips|KS005|Phillips|20147|C|nc|39.7845|-99.3469
KS|006|GID|Smith|KS006|Smith|20183|C|nc|39.7851|-98.7855
KS|007|GID|Jewell|KS007|Jewell|20089|C|nc|39.7847|-98.2184
KS|017|GID|Rooks|KS017|Rooks|20163|C|nc|39.3501|-99.3251
KS|018|GID|Osborne|KS018|Osborne|20141|C|nc|39.3503|-98.7679
KS|019|GID|Mitchell|KS019|Mitchell|20123|C|nc|39.3933|-98.2095
NE|039|GID|Valley|NE039|Valley|31175|C|cc|41.5673|-98.9819
NE|040|GID|Greeley|NE040|Greeley|31077|C|cc|41.5675|-98.5212
NE|041|GID|Nance|NE041|Nance|31125|C|cc|41.3973|-97.9923
NE|046|GID|Sherman|NE046|Sherman|31163|C|cc|41.2205|-98.9763
NE|047|GID|Howard|NE047|Howard|31093|C|cc|41.22|-98.5171
NE|048|GID|Merrick|NE048|Merrick|31121|C|cc|41.1698|-98.0376
NE|049|GID|Polk|NE049|Polk|31143|C|ec|41.1869|-97.5684
NE|060|GID|Dawson|NE060|Dawson|31047|C|sc|40.8699|-99.8195
NE|061|GID|Buffalo|NE061|Buffalo|31019|C|sc|40.8551|-99.075
NE|062|GID|Hall|NE062|Hall|31079|C|sc|40.8725|-98.5022
NE|063|GID|Hamilton|NE063|Hamilton|31081|C|sc|40.8735|-98.0233
NE|064|GID|York|NE064|York|31185|C|ec|40.8728|-97.5971
NE|072|GID|Gosper|NE072|Gosper|31073|C|sc|40.5148|-99.8307
NE|073|GID|Phelps|NE073|Phelps|31137|C|sc|40.5111|-99.4145
NE|074|GID|Kearney|NE074|Kearney|31099|C|sc|40.5067|-98.948
NE|075|GID|Adams|NE075|Adams|31001|C|sc|40.5245|-98.5012
NE|076|GID|Clay|NE076|Clay|31035|C|sc|40.5244|-98.0512
NE|077|GID|Fillmore|NE077|Fillmore|31059|C|sc|40.5247|-97.5965
NE|082|GID|Furnas|NE082|Furnas|31065|C|sc|40.1764|-99.9123
NE|083|GID|Harlan|NE083|Harlan|31083|C|sc|40.1765|-99.4046
NE|084|GID|Franklin|NE084|Franklin|31061|C|sc|40.1763|-98.9527
NE|085|GID|Webster|NE085|Webster|31181|C|sc|40.1764|-98.4999
NE|086|GID|Nuckolls|NE086|Nuckolls|31129|C|sc|40.1764|-98.0472
NE|087|GID|Thayer|NE087|Thayer|31169|C|sc|40.1763|-97.5948
CO|001|GJT|Lower Yampa River Basin|CO001|Garfield|08045|M|wc|40.444|-108.6994
CO|001|GJT|Lower Yampa River Basin|CO001|Moffat|08081|M|nw|40.444|-108.6994
CO|001|GJT|Lower Yampa River Basin|CO001|Rio Blanco|08103|M|nw|40.444|-108.6994
CO|002|GJT|Central Yampa River Basin|CO002|Moffat|08081|M|nw|40.4046|-107.9134
CO|002|GJT|Central Yampa River Basin|CO002|Rio Blanco|08103|M|nw|40.4046|-107.9134
CO|002|GJT|Central Yampa River Basin|CO002|Routt|08107|M|nw|40.4046|-107.9134
CO|003|GJT|Roan and Tavaputs Plateaus|CO003|Garfield|08045|M|wc|39.5758|-108.4377
CO|003|GJT|Roan and Tavaputs Plateaus|CO003|Mesa|08077|M|wc|39.5758|-108.4377
CO|003|GJT|Roan and Tavaputs Plateaus|CO003|Rio Blanco|08103|M|nw|39.5758|-108.4377
CO|004|GJT|Elkhead and Park Mountains|CO004|Moffat|08081|M|nw|40.5653|-106.9552
CO|004|GJT|Elkhead and Park Mountains|CO004|Routt|08107|M|nw|40.5653|-106.9552
CO|005|GJT|Upper Yampa River Basin|CO005|Routt|08107|M|nw|40.3903|-106.9616
CO|006|GJT|Grand Valley|CO006|Garfield|08045|M|wc|39.1541|-108.6809
CO|006|GJT|Grand Valley|CO006|Mesa|08077|M|wc|39.1541|-108.6809
CO|007|GJT|Debeque to Silt Corridor|CO007|Garfield|08045|M|wc|39.4422|-107.9773
CO|007|GJT|Debeque to Silt Corridor|CO007|Mesa|08077|M|wc|39.4422|-107.9773
CO|008|GJT|Central Colorado River Basin|CO008|Eagle|08037|M|cc|39.6286|-107.0292
CO|008|GJT|Central Colorado River Basin|CO008|Garfield|08045|M|wc|39.6286|-107.0292
CO|008|GJT|Central Colorado River Basin|CO008|Pitkin|08097|M|cc|39.6286|-107.0292
CO|009|GJT|Grand and Battlement Mesas|CO009|Delta|08029|M|wc|39.1332|-107.8549
CO|009|GJT|Grand and Battlement Mesas|CO009|Garfield|08045|M|wc|39.1332|-107.8549
CO|009|GJT|Grand and Battlement Mesas|CO009|Mesa|08077|M|wc|39.1332|-107.8549
CO|010|GJT|Gore and Elk Mountains/Central Mountain Valleys|CO010|Eagle|08037|M|cc|39.4353|-106.8147
CO|010|GJT|Gore and Elk Mountains/Central Mountain Valleys|CO010|Garfield|08045|M|wc|39.4353|-106.8147
CO|010|GJT|Gore and Elk Mountains/Central Mountain Valleys|CO010|Pitkin|08097|M|cc|39.4353|-106.8147
CO|011|GJT|Central Gunnison and Uncompahgre River Basin|CO011|Delta|08029|M|wc|38.6735|-107.9201
CO|011|GJT|Central Gunnison and Uncompahgre River Basin|CO011|Gunnison|08051|M|cc|38.6735|-107.9201
CO|011|GJT|Central Gunnison and Uncompahgre River Basin|CO011|Mesa|08077|M|wc|38.6735|-107.9201
CO|011|GJT|Central Gunnison and Uncompahgre River Basin|CO011|Montrose|08085|M|wc|38.6735|-107.9201
CO|012|GJT|West Elk and Sawatch Mountains|CO012|Delta|08029|M|wc|38.8011|-107.0042
CO|012|GJT|West Elk and Sawatch Mountains|CO012|Gunnison|08051|M|cc|38.8011|-107.0042
CO|012|GJT|West Elk and Sawatch Mountains|CO012|Montrose|08085|M|wc|38.8011|-107.0042
CO|013|GJT|Flattops|CO013|Eagle|08037|M|cc|39.9766|-107.4376
CO|013|GJT|Flattops|CO013|Garfield|08045|M|wc|39.9766|-107.4376
CO|013|GJT|Flattops|CO013|Moffat|08081|M|nw|39.9766|-107.4376
CO|013|GJT|Flattops|CO013|Rio Blanco|08103|M|nw|39.9766|-107.4376
CO|013|GJT|Flattops|CO013|Routt|08107|M|nw|39.9766|-107.4376
CO|014|GJT|Upper Gunnison River Valley|CO014|Gunnison|08051|M|cc|38.4776|-107.1881
CO|014|GJT|Upper Gunnison River Valley|CO014|Montrose|08085|M|wc|38.4776|-107.1881
CO|017|GJT|Uncompahgre Plateu/Dallas Divide|CO017|Delta|08029|M|wc|38.5539|-108.4296
CO|017|GJT|Uncompahgre Plateu/Dallas Divide|CO017|Mesa|08077|M|wc|38.5539|-108.4296
CO|017|GJT|Uncompahgre Plateu/Dallas Divide|CO017|Montrose|08085|M|wc|38.5539|-108.4296
CO|017|GJT|Uncompahgre Plateu/Dallas Divide|CO017|Ouray|08091|M|sw|38.5539|-108.4296
CO|017|GJT|Uncompahgre Plateu/Dallas Divide|CO017|San Miguel|08113|M|wc|38.5539|-108.4296
CO|018|GJT|Northwestern San Juan Mountains|CO018|Gunnison|08051|M|cc|38.0588|-107.5504
CO|018|GJT|Northwestern San Juan Mountains|CO018|Hinsdale|08053|M|sw|38.0588|-107.5504
CO|018|GJT|Northwestern San Juan Mountains|CO018|Montrose|08085|M|wc|38.0588|-107.5504
CO|018|GJT|Northwestern San Juan Mountains|CO018|Ouray|08091|M|sw|38.0588|-107.5504
CO|018|GJT|Northwestern San Juan Mountains|CO018|San Miguel|08113|M|wc|38.0588|-107.5504
CO|019|GJT|Southwest San Juan Mountains|CO019|Archuleta|08007|M|sc|37.5206|-107.6597
CO|019|GJT|Southwest San Juan Mountains|CO019|Dolores|08033|M|sw|37.5206|-107.6597
CO|019|GJT|Southwest San Juan Mountains|CO019|Hinsdale|08053|M|sw|37.5206|-107.6597
CO|019|GJT|Southwest San Juan Mountains|CO019|La Plata|08067|M|sw|37.5206|-107.6597
CO|019|GJT|Southwest San Juan Mountains|CO019|Montezuma|08083|M|sw|37.5206|-107.6597
CO|019|GJT|Southwest San Juan Mountains|CO019|San Juan|08111|M|se|37.5206|-107.6597
CO|019|GJT|Southwest San Juan Mountains|CO019|San Miguel|08113|M|wc|37.5206|-107.6597
CO|020|GJT|Paradox Valley/Little Dolores River|CO020|Dolores|08033|M|sw|38.1963|-108.7095
CO|020|GJT|Paradox Valley/Little Dolores River|CO020|Mesa|08077|M|wc|38.1963|-108.7095
CO|020|GJT|Paradox Valley/Little Dolores River|CO020|Montrose|08085|M|wc|38.1963|-108.7095
CO|020|GJT|Paradox Valley/Little Dolores River|CO020|San Miguel|08113|M|wc|38.1963|-108.7095
CO|021|GJT|Four Corners/Upper Dolores River|CO021|Dolores|08033|M|sw|37.3809|-108.7278
CO|021|GJT|Four Corners/Upper Dolores River|CO021|Montezuma|08083|M|sw|37.3809|-108.7278
CO|021|GJT|Four Corners/Upper Dolores River|CO021|San Miguel|08113|M|wc|37.3809|-108.7278
CO|022|GJT|Animas River Basin|CO022|La Plata|08067|M|sw|37.1488|-107.8775
CO|023|GJT|San Juan River Basin|CO023|Archuleta|08007|M|sc|37.1383|-107.2004
UT|022|GJT|Southeast Utah|UT022|San Juan|49037|M|se|37.2729|-109.6517
UT|023|GJT|Eastern Unita Mountains|UT023|Daggett|49009|M|ne|40.7677|-109.5041
UT|023|GJT|Eastern Unita Mountains|UT023|Uintah|49047|M|ne|40.7677|-109.5041
UT|024|GJT|Eastern Uinta Basin|UT024|Uintah|49047|M|ne|40.2152|-109.538
UT|025|GJT|Tavaputs Plateau|UT025|Grand|49019|M|ec|39.4851|-109.5696
UT|025|GJT|Tavaputs Plateau|UT025|Uintah|49047|M|ne|39.4851|-109.5696
UT|027|GJT|Arches/Grand Flat|UT027|Grand|49019|M|ec|38.8582|-109.5593
UT|028|GJT|La Sal and Abajo Mountains|UT028|Grand|49019|M|ec|38.047|-109.3836
UT|028|GJT|La Sal and Abajo Mountains|UT028|San Juan|49037|M|se|38.047|-109.3836
UT|029|GJT|Canyonlands/Natural Bridges|UT029|San Juan|49037|M|se|37.8442|-110.0067
CO|090|GLD|Yuma County|CO090|Yuma|08125|M|ne|40.0029|-102.4243
CO|091|GLD|Kit Carson County|CO091|Kit Carson|08063|M|ec|39.3054|-102.6029
CO|092|GLD|Cheyenne County|CO092|Cheyenne|08017|M|ec|38.8279|-102.6034
KS|001|GLD|Cheyenne|KS001|Cheyenne|20023|C|nw|39.7858|-101.7312
KS|002|GLD|Rawlins|KS002|Rawlins|20153|C|nw|39.7852|-101.0758
KS|003|GLD|Decatur|KS003|Decatur|20039|C|nw|39.7847|-100.4599
KS|004|GLD|Norton|KS004|Norton|20137|C|nw|39.7844|-99.9034
KS|013|GLD|Sherman|KS013|Sherman|20181|M|nw|39.3514|-101.72
KS|014|GLD|Thomas|KS014|Thomas|20193|C|nw|39.3509|-101.0555
KS|015|GLD|Sheridan|KS015|Sheridan|20179|C|nw|39.3503|-100.4418
KS|016|GLD|Graham|KS016|Graham|20065|C|nw|39.3497|-99.8833
KS|027|GLD|Wallace|KS027|Wallace|20199|M|wc|38.9166|-101.7636
KS|028|GLD|Logan|KS028|Logan|20109|C|wc|38.9173|-101.1485
KS|029|GLD|Gove|KS029|Gove|20063|C|wc|38.9161|-100.4829
KS|041|GLD|Greeley|KS041|Greeley|20071|M|wc|38.4805|-101.806
KS|042|GLD|Wichita|KS042|Wichita|20203|C|wc|38.4821|-101.3474
NE|079|GLD|Dundy|NE079|Dundy|31057|M|sw|40.1762|-101.6879
NE|080|GLD|Hitchcock|NE080|Hitchcock|31087|C|sw|40.1763|-101.0422
NE|081|GLD|Red Willow|NE081|Red Willow|31145|C|sw|40.1758|-100.4768
WI|005|GRB|Vilas|WI005|Vilas|55125|C|nc|46.0529|-89.5148
WI|010|GRB|Oneida|WI010|Oneida|55085|C|nc|45.7056|-89.5217
WI|011|GRB|Forest|WI011|Forest|55041|C|ne|45.6673|-88.7704
WI|012|GRB|Florence|WI012|Florence|55037|C|ne|45.8484|-88.3982
WI|013|GRB|Northern Marinette County|WI013|Marinette|55075|C|ne|45.5511|-88.109
WI|018|GRB|Lincoln|WI018|Lincoln|55069|C|nc|45.3375|-89.7346
WI|019|GRB|Langlade|WI019|Langlade|55067|C|nc|45.2624|-89.0719
WI|020|GRB|Menominee|WI020|Menominee|55078|C|ne|45.0044|-88.71
WI|021|GRB|Northern Oconto County|WI021|Oconto|55083|C|ne|45.2006|-88.4257
WI|022|GRB|Door|WI022|Door|55029|C|ne|44.9435|-87.3173
WI|030|GRB|Marathon|WI030|Marathon|55073|C|cc|44.8983|-89.759
WI|031|GRB|Shawano|WI031|Shawano|55115|C|ne|44.7892|-88.7656
WI|035|GRB|Wood|WI035|Wood|55141|C|cc|44.4553|-90.0416
WI|036|GRB|Portage|WI036|Portage|55097|C|cc|44.476|-89.5015
WI|037|GRB|Waupaca|WI037|Waupaca|55135|C|ne|44.4704|-88.9648
WI|038|GRB|Outagamie|WI038|Outagamie|55087|C|ne|44.4161|-88.4649
WI|039|GRB|Brown|WI039|Brown|55009|C|ne|44.4537|-88.0032
WI|040|GRB|Kewaunee|WI040|Kewaunee|55061|C|ne|44.5161|-87.6154
WI|045|GRB|Waushara|WI045|Waushara|55137|C|cc|44.1131|-89.2429
WI|048|GRB|Winnebago|WI048|Winnebago|55139|C|ec|44.0689|-88.6446
WI|049|GRB|Calumet|WI049|Calumet|55015|C|ec|44.0817|-88.218
WI|050|GRB|Manitowoc|WI050|Manitowoc|55071|C|ec|44.1198|-87.8096
WI|073|GRB|Southern Marinette County|WI073|Marinette|55075|C|ne|45.1874|-87.9475
WI|074|GRB|Southern Oconto County|WI074|Oconto|55083|C|ne|44.8829|-88.139
MI|037|GRR|Mason|MI037|Mason|26105|E|wc|43.9954|-86.2497
MI|038|GRR|Lake|MI038|Lake|26085|E|wc|43.99|-85.8017
MI|039|GRR|Osceola|MI039|Osceola|26133|E|cc|43.9899|-85.3252
MI|040|GRR|Clare|MI040|Clare|26035|E|cc|43.9879|-84.8478
MI|043|GRR|Oceana|MI043|Oceana|26127|E|wc|43.6407|-86.2673
MI|044|GRR|Newaygo|MI044|Newaygo|26123|E|wc|43.5542|-85.8009
MI|045|GRR|Mecosta|MI045|Mecosta|26107|E|cc|43.6409|-85.3245
MI|046|GRR|Isabella|MI046|Isabella|26073|E|cc|43.6406|-84.8467
MI|050|GRR|Muskegon|MI050|Muskegon|26121|E|wc|43.2912|-86.1481
MI|051|GRR|Montcalm|MI051|Montcalm|26117|E|cc|43.311|-85.1524
MI|052|GRR|Gratiot|MI052|Gratiot|26057|E|cc|43.2927|-84.6048
MI|056|GRR|Ottawa|MI056|Ottawa|26139|E|sw|42.9601|-85.9939
MI|057|GRR|Kent|MI057|Kent|26081|E|sw|43.0322|-85.5492
MI|058|GRR|Ionia|MI058|Ionia|26067|E|sc|42.9451|-85.0746
MI|059|GRR|Clinton|MI059|Clinton|26037|E|sc|42.9436|-84.6015
MI|064|GRR|Allegan|MI064|Allegan|26005|E|sw|42.5913|-85.8884
MI|065|GRR|Barry|MI065|Barry|26015|E|sw|42.595|-85.309
MI|066|GRR|Eaton|MI066|Eaton|26045|E|sc|42.5961|-84.8384
MI|067|GRR|Ingham|MI067|Ingham|26065|E|sc|42.5971|-84.3736
MI|071|GRR|Van Buren|MI071|Van Buren|26159|E|sw|42.2513|-86.0189
MI|072|GRR|Kalamazoo|MI072|Kalamazoo|26077|E|sw|42.2454|-85.5312
MI|073|GRR|Calhoun|MI073|Calhoun|26025|E|sc|42.2466|-85.0055
MI|074|GRR|Jackson|MI074|Jackson|26075|E|sc|42.2485|-84.4233
GA|010|GSP|Rabun|GA010|Rabun|13241|E|ne|34.8818|-83.4021
GA|017|GSP|Habersham|GA017|Habersham|13137|E|ne|34.631|-83.5312
GA|018|GSP|Stephens|GA018|Stephens|13257|E|ne|34.554|-83.2935
GA|026|GSP|Franklin|GA026|Franklin|13119|E|ne|34.3755|-83.2292
GA|028|GSP|Hart|GA028|Hart|13147|E|ne|34.3511|-82.964
GA|029|GSP|Elbert|GA029|Elbert|13105|E|ne|34.1169|-82.8403
NC|033|GSP|Avery|NC033|Avery|37011|E|ww|36.0766|-81.9224
NC|035|GSP|Alexander|NC035|Alexander|37003|E|pd|35.9211|-81.1772
NC|036|GSP|Iredell|NC036|Iredell|37097|E|pd|35.8072|-80.8736
NC|037|GSP|Davie|NC037|Davie|37059|E|pd|35.9292|-80.5446
NC|048|GSP|Madison|NC048|Madison|37115|E|ww|35.8581|-82.7057
NC|049|GSP|Yancey|NC049|Yancey|37199|E|ww|35.8989|-82.3076
NC|050|GSP|Mitchell|NC050|Mitchell|37121|E|ww|36.0133|-82.1634
NC|051|GSP|Swain|NC051|Swain|37173|E|ww|35.4867|-83.4927
NC|052|GSP|Haywood|NC052|Haywood|37087|E|ww|35.5561|-82.9822
NC|053|GSP|Buncombe|NC053|Buncombe|37021|E|ww|35.6112|-82.5302
NC|056|GSP|Catawba|NC056|Catawba|37035|E|pd|35.6626|-81.2144
NC|057|GSP|Rowan|NC057|Rowan|37159|E|pd|35.6396|-80.5247
NC|058|GSP|Graham|NC058|Graham|37075|E|ww|35.3502|-83.8335
NC|059|GSP|Northern Jackson|NC059|Jackson|37099|E|ww|35.3638|-83.1778
NC|062|GSP|Macon|NC062|Macon|37113|E|ww|35.1504|-83.4221
NC|063|GSP|Southern Jackson|NC063|Jackson|37099|E|ww|35.1614|-83.0799
NC|064|GSP|Transylvania|NC064|Transylvania|37175|E|ww|35.2022|-82.7983
NC|065|GSP|Henderson|NC065|Henderson|37089|E|ww|35.3362|-82.4799
NC|068|GSP|Cleveland|NC068|Cleveland|37045|E|pd|35.334|-81.5554
NC|069|GSP|Lincoln|NC069|Lincoln|37109|E|pd|35.4862|-81.2239
NC|070|GSP|Gaston|NC070|Gaston|37071|E|pd|35.2945|-81.1801
NC|071|GSP|Mecklenburg|NC071|Mecklenburg|37119|E|pd|35.2468|-80.8328
NC|072|GSP|Cabarrus|NC072|Cabarrus|37025|E|pd|35.3868|-80.5519
NC|082|GSP|Union|NC082|Union|37179|E|pd|34.9884|-80.5307
NC|501|GSP|Caldwell Mountains|NC501|Caldwell|37027|E|ww|36.0301|-81.6408
NC|502|GSP|Greater Caldwell|NC502|Caldwell|37027|E|ww|35.9012|-81.4832
NC|503|GSP|Burke Mountains|NC503|Burke|37023|E|ww|35.8886|-81.862
NC|504|GSP|Greater Burke|NC504|Burke|37023|E|ww|35.7148|-81.6652
NC|505|GSP|McDowell Mountains|NC505|McDowell|37111|E|ww|35.7082|-82.1054
NC|506|GSP|Eastern McDowell|NC506|McDowell|37111|E|ww|35.6327|-81.9458
NC|507|GSP|Rutherford Mountains|NC507|Rutherford|37161|E|ww|35.465|-82.193
NC|508|GSP|Greater Rutherford|NC508|Rutherford|37161|E|ww|35.3952|-81.8892
NC|509|GSP|Polk Mountains|NC509|Polk|37149|E|ww|35.2856|-82.293
NC|510|GSP|Eastern Polk|NC510|Polk|37149|E|ww|35.2776|-82.1356
SC|008|GSP|Cherokee|SC008|Cherokee|45021|E|up|35.0482|-81.6204
SC|009|GSP|York|SC009|York|45091|E|up|34.9747|-81.1845
SC|010|GSP|Anderson|SC010|Anderson|45007|E|up|34.5191|-82.6379
SC|011|GSP|Abbeville|SC011|Abbeville|45001|E|up|34.2226|-82.4587
SC|012|GSP|Laurens|SC012|Laurens|45059|E|up|34.4836|-82.006
SC|013|GSP|Union|SC013|Union|45087|E|up|34.6892|-81.6194
SC|014|GSP|Chester|SC014|Chester|45023|E|up|34.6921|-81.1595
SC|019|GSP|Greenwood|SC019|Greenwood|45047|E|up|34.1538|-82.1259
SC|101|GSP|Oconee Mountains|SC101|Oconee|45073|E||34.8778|-83.1175
SC|102|GSP|Pickens Mountains|SC102|Pickens|45077|E||35.0173|-82.8101
SC|103|GSP|Greenville Mountains|SC103|Greenville|45045|E|up|35.13|-82.4629
SC|104|GSP|Greater Oconee|SC104|Oconee|45073|E||34.6875|-83.0385
SC|105|GSP|Greater Pickens|SC105|Pickens|45077|E||34.8593|-82.7069
SC|106|GSP|Central Greenville|SC106|Greenville|45045|E||34.9673|-82.3782
SC|107|GSP|Southern Greenville|SC107|Greenville|45045|E|up|34.6832|-82.3139
SC|108|GSP|Northern Spartanburg|SC108|Spartanburg|45083|E|up|35.0656|-82.0536
SC|109|GSP|Southern Spartanburg|SC109|Spartanburg|45083|E|up|34.8324|-81.9443
GU|001|GUM|Guam|GU001|Guam|66010|G||13.4435|144.7774
MP|001|GUM|Rota|MP001|Rota|69100|G||14.1576|145.2148
MP|002|GUM|Tinian|MP002|Tinian|69120|G||15.003|145.6267
MP|003|GUM|Saipan|MP003|Saipan|69110|G||15.1889|145.7534
MP|004|GUM|Anatahan|MP004|Anatahan|69085|G||16.3519|145.6774
MP|005|GUM|Alamagan|MP005|Alamagan|69085|G||17.5998|145.833
MP|006|GUM|Pagan|MP006|Pagan|69085|G||18.1166|145.7666
MP|007|GUM|Agrihan|MP007|Agrihan|69085|G||18.771|145.6674
ME|007|GYX|Northern Oxford|ME007|Oxford|23017|E|ww|44.8431|-70.8789
ME|008|GYX|Northern Franklin|ME008|Franklin|23007|E|ww|45.0717|-70.5249
ME|009|GYX|Central Somerset|ME009|Somerset|23025|E|wc|45.48|-70.068
ME|012|GYX|Southern Oxford|ME012|Oxford|23017|E|ww|44.2631|-70.6709
ME|013|GYX|Southern Franklin|ME013|Franklin|23007|E|ww|44.6571|-70.1818
ME|014|GYX|Southern Somerset|ME014|Somerset|23025|E|wc|44.8398|-69.6632
ME|018|GYX|Interior York|ME018|York|23031|E|sw|43.559|-70.7784
ME|019|GYX|Central Interior Cumberland|ME019|Cumberland|23005|E||43.8563|-70.4616
ME|020|GYX|Androscoggin|ME020|Androscoggin|23001|E|sw|44.1654|-70.2045
ME|021|GYX|Kennebec|ME021|Kennebec|23011|E|sc|44.4093|-69.7672
ME|022|GYX|Interior Waldo|ME022|Waldo|23027|E|sc|44.5406|-69.1709
ME|023|GYX|Coastal York|ME023|York|23031|E|sw|43.3339|-70.6005
ME|024|GYX|Coastal Cumberland|ME024|Cumberland|23005|E||43.7449|-70.186
ME|025|GYX|Sagadahoc|ME025|Sagadahoc|23023|E|sc|43.9705|-69.8613
ME|026|GYX|Lincoln|ME026|Lincoln|23015|E|sc|44.0752|-69.5431
ME|027|GYX|Knox|ME027|Knox|23013|E|sc|44.15|-69.173
ME|028|GYX|Coastal Waldo|ME028|Waldo|23027|E|sc|44.349|-69.0512
ME|033|GYX|Interior Cumberland Highlands|ME033|Cumberland|23005|E||44.0404|-70.6904
NH|001|GYX|Northern Coos|NH001|Coos|33007|E|nn|44.9761|-71.2832
NH|002|GYX|Southern Coos|NH002|Coos|33007|E|nn|44.4715|-71.3228
NH|003|GYX|Northern Grafton|NH003|Grafton|33009|E|nn|44.0964|-71.7514
NH|004|GYX|Northern Carroll|NH004|Carroll|33003|E|nn|44.078|-71.1778
NH|005|GYX|Southern Grafton|NH005|Grafton|33009|E|nn|43.7209|-71.9182
NH|006|GYX|Southern Carroll|NH006|Carroll|33003|E|nn|43.7506|-71.2178
NH|007|GYX|Sullivan|NH007|Sullivan|33019|E|cc|43.3612|-72.2223
NH|008|GYX|Merrimack|NH008|Merrimack|33013|E|cc|43.2977|-71.6802
NH|009|GYX|Belknap|NH009|Belknap|33001|E|cc|43.5188|-71.4233
NH|010|GYX|Strafford|NH010|Strafford|33017|E|cc|43.2975|-71.0293
NH|013|GYX|Interior Rockingham|NH013|Rockingham|33015|E|ss|42.9853|-71.1814
NH|014|GYX|Coastal Rockingham|NH014|Rockingham|33015|E|ss|43.0005|-70.8291
HI|001|HFO|Niihau|HI001|Kauai|15007|H||21.897|-160.157
HI|003|HFO|Kauai Southwest|HI003|Kauai|15007|H||22.0073|-159.6639
HI|004|HFO|Kauai Mountains|HI004|Kauai|15007|H||22.0963|-159.543
HI|006|HFO|Waianae Coast|HI006|Honolulu|15003|H||21.4436|-158.1698
HI|007|HFO|Oahu North Shore|HI007|Honolulu|15003|H||21.5991|-158.1007
HI|009|HFO|Olomana|HI009|Honolulu|15003|H||21.3809|-157.7459
HI|010|HFO|Central Oahu|HI010|Honolulu|15003|H||21.4843|-158.027
HI|011|HFO|Waianae Mountains|HI011|Honolulu|15003|H||21.4683|-158.1327
HI|015|HFO|Lanai Mauka|HI015|Maui|15009|H||20.8177|-156.9138
HI|016|HFO|Kahoolawe|HI016|Maui|15009|H||20.5503|-156.6118
HI|017|HFO|Maui Windward West|HI017|Maui|15009|H||20.9195|-156.5762
HI|018|HFO|Maui Leeward West|HI018|Maui|15009|H||20.8913|-156.6446
HI|022|HFO|Haleakala Summit|HI022|Maui|15009|H||20.7202|-156.2248
HI|023|HFO|Kona|HI023|Hawaii|15001|H||19.4131|-155.8806
HI|026|HFO|Kohala|HI026|Hawaii|15001|H||19.8824|-155.8068
HI|027|HFO|Big Island Interior|HI027|Hawaii|15001|H||19.5822|-155.5756
HI|028|HFO|Big Island Summit|HI028|Hawaii|15001|H||19.5563|-155.555
HI|029|HFO|Kauai North|HI029|Kauai|15007|H||22.1834|-159.5254
HI|030|HFO|Kauai East|HI030|Kauai|15007|H||22.049|-159.3899
HI|031|HFO|Kauai South|HI031|Kauai|15007|H||21.914|-159.4781
HI|032|HFO|East Honolulu|HI032|Honolulu|15003|H||21.2897|-157.726
HI|033|HFO|Honolulu Metro|HI033|Honolulu|15003|H||21.3203|-157.8849
HI|034|HFO|Ewa Plain|HI034|Honolulu|15003|H||21.3526|-158.0226
HI|035|HFO|Koolau Windward|HI035|Honolulu|15003|H||21.5539|-157.9014
HI|036|HFO|Koolau Leeward|HI036|Honolulu|15003|H||21.4387|-157.8915
HI|037|HFO|Molokai Windward|HI037|Maui|15009|H||21.1494|-156.8556
HI|038|HFO|Molokai Southeast|HI038|Maui|15009|H||21.097|-156.8249
HI|039|HFO|Molokai North|HI039|Maui|15009|H||21.1843|-157.0947
HI|040|HFO|Molokai West|HI040|Maui|15009|H||21.1572|-157.2611
HI|041|HFO|Molokai Leeward South|HI041|Maui|15009|H||21.1257|-157.0866
HI|042|HFO|Lanai Windward|HI042|Maui|15009|H||20.8828|-156.9154
HI|043|HFO|Lanai Leeward|HI043|Maui|15009|H||20.842|-157.0005
HI|044|HFO|Lanai South|HI044|Maui|15009|H||20.7633|-156.8905
HI|045|HFO|Maui Central Valley North|HI045|Maui|15009|H||20.8708|-156.4171
HI|046|HFO|Maui Central Valley South|HI046|Maui|15009|H||20.8082|-156.4688
HI|047|HFO|Windward Haleakala|HI047|Maui|15009|H||20.8318|-156.194
HI|048|HFO|Kipahulu|HI048|Maui|15009|H||20.7034|-156.0527
HI|049|HFO|South Maui/Upcountry|HI049|Maui|15009|H||20.7293|-156.3795
HI|050|HFO|South Haleakala|HI050|Hawaii|15001|H||20.6382|-156.2465
HI|051|HFO|Big Island South|HI051|Hawaii|15001|H||19.0603|-155.7364
HI|052|HFO|Big Island Southeast|HI052|Hawaii|15001|H||19.2625|-155.3822
HI|053|HFO|Big Island East|HI053|Hawaii|15001|H||19.6291|-155.1341
HI|054|HFO|Big Island North|HI054|Hawaii|15001|H||20.0641|-155.596
TX|163|HGX|Houston|TX163|Houston|48225|C|se|31.3178|-95.4227
TX|164|HGX|Trinity|TX164|Trinity|48455|C|se|31.0888|-95.1355
TX|176|HGX|Madison|TX176|Madison|48313|C|se|30.9656|-95.9284
TX|177|HGX|Walker|TX177|Walker|48471|C|se|30.739|-95.5722
TX|178|HGX|San Jancinto|TX178|San Jacinto|48407|C|se|30.5796|-95.1669
TX|179|HGX|Polk|TX179|Polk|48373|C|se|30.7928|-94.83
TX|195|HGX|Burleson|TX195|Burleson|48051|C|se|30.4924|-96.621
TX|196|HGX|Brazos|TX196|Brazos|48041|C|se|30.6611|-96.3023
TX|197|HGX|Washington|TX197|Washington|48477|C|se|30.2145|-96.4036
TX|198|HGX|Grimes|TX198|Grimes|48185|C|se|30.5436|-95.9855
TX|199|HGX|Montgomery|TX199|Montgomery|48339|C|se|30.3002|-95.503
TX|200|HGX|Northern Liberty|TX200|Liberty|48291|C|se|30.2284|-94.8693
TX|210|HGX|Colorado|TX210|Colorado|48089|C|se|29.6208|-96.5263
TX|211|HGX|Austin|TX211|Austin|48015|C|se|29.887|-96.278
TX|212|HGX|Waller|TX212|Waller|48473|C|se|30.0111|-95.9877
TX|213|HGX|Inland Harris|TX213|Harris|48201|C|se|29.8829|-95.459
TX|214|HGX|Chambers|TX214|Chambers|48071|C|se|29.7388|-94.608
TX|226|HGX|Wharton|TX226|Wharton|48481|C|se|29.2779|-96.2221
TX|227|HGX|Fort Bend|TX227|Fort Bend|48157|C|se|29.5274|-95.7707
TX|235|HGX|Inland Jackson|TX235|Jackson|48239|C|sc|29.0039|-96.6044
TX|236|HGX|Inland Matagorda|TX236|Matagorda|48321|C|se|28.9561|-96.0201
TX|237|HGX|Inland Brazoria|TX237|Brazoria|48039|C|se|29.269|-95.5128
TX|238|HGX|Inland Galveston|TX238|Galveston|48167|C|se|29.4207|-95.132
TX|300|HGX|Southern Liberty|TX300|Liberty|48291|C|se|29.9703|-94.6771
TX|313|HGX|Coastal Harris|TX313|Harris|48201|C|se|29.7281|-95.0568
TX|335|HGX|Coastal Jackson|TX335|Jackson|48239|C|sc|28.7655|-96.4773
TX|336|HGX|Coastal Matagorda|TX336|Matagorda|48321|C|se|28.7695|-95.9366
TX|337|HGX|Coastal Brazoria|TX337|Brazoria|48039|C|se|29.0676|-95.3623
TX|338|HGX|Coastal Galveston|TX338|Galveston|48167|C|se|29.3887|-95.0028
TX|436|HGX|Matagorda Islands|TX436|Matagorda|48321|C|se|28.6248|-95.9674
TX|437|HGX|Brazoria Islands|TX437|Brazoria|48039|C|se|28.9671|-95.3005
TX|438|HGX|Galveston Island|TX438|Galveston|48167|C|se|29.2456|-94.8973
TX|439|HGX|Bolivar Peninsula|TX439|Galveston|48167|C|se|29.4886|-94.5711
CA|300|HNX|West Side Mountains north of 198|CA300|Fresno|06019|P|cc|36.6593|-120.7869
CA|300|HNX|West Side Mountains north of 198|CA300|Merced|06047|P|cc|36.6593|-120.7869
CA|301|HNX|Los Banos - Dos Palos|CA301|Fresno|06019|P|cc|36.9125|-120.7212
CA|301|HNX|Los Banos - Dos Palos|CA301|Merced|06047|P|cc|36.9125|-120.7212
CA|302|HNX|Merced - Madera - Mendota|CA302|Fresno|06019|P|cc|37.0903|-120.4536
CA|302|HNX|Merced - Madera - Mendota|CA302|Madera|06039|P|cc|37.0903|-120.4536
CA|302|HNX|Merced - Madera - Mendota|CA302|Merced|06047|P|cc|37.0903|-120.4536
CA|303|HNX|Planada - Le Grand - Snelling|CA303|Madera|06039|P|cc|37.2577|-120.193
CA|303|HNX|Planada - Le Grand - Snelling|CA303|Mariposa|06043|P|cc|37.2577|-120.193
CA|303|HNX|Planada - Le Grand - Snelling|CA303|Merced|06047|P|cc|37.2577|-120.193
CA|304|HNX|Coalinga - Avenal|CA304|Fresno|06019|P|cc|36.0678|-120.1879
CA|304|HNX|Coalinga - Avenal|CA304|Kings|06031|P|cc|36.0678|-120.1879
CA|305|HNX|West Side of Fresno and Kings Counties|CA305|Fresno|06019|P|cc|36.287|-120.1034
CA|305|HNX|West Side of Fresno and Kings Counties|CA305|Kings|06031|P|cc|36.287|-120.1034
CA|306|HNX|Caruthers - San Joaquin - Selma|CA306|Fresno|06019|P|cc|36.5869|-119.8953
CA|306|HNX|Caruthers - San Joaquin - Selma|CA306|Tulare|06107|P|cc|36.5869|-119.8953
CA|307|HNX|Fresno-Clovis|CA307|Fresno|06019|P|cc|36.7953|-119.7342
CA|308|HNX|West Side Mountains South of 198|CA308|Fresno|06019|P|cc|35.6837|-120.0363
CA|308|HNX|West Side Mountains South of 198|CA308|Kern|06029|P|cc|35.6837|-120.0363
CA|308|HNX|West Side Mountains South of 198|CA308|Kings|06031|P|cc|35.6837|-120.0363
CA|309|HNX|Buttonwillow - Lost Hills - I5|CA309|Kern|06029|P|cc|35.6098|-119.6082
CA|309|HNX|Buttonwillow - Lost Hills - I5|CA309|Kings|06031|P|cc|35.6098|-119.6082
CA|310|HNX|Delano-Wasco-Shafter|CA310|Kern|06029|P|cc|35.7752|-119.3702
CA|310|HNX|Delano-Wasco-Shafter|CA310|Kings|06031|P|cc|35.7752|-119.3702
CA|310|HNX|Delano-Wasco-Shafter|CA310|Tulare|06107|P|cc|35.7752|-119.3702
CA|311|HNX|Hanford - Corcoran - Lemoore|CA311|Fresno|06019|P|cc|36.226|-119.5882
CA|311|HNX|Hanford - Corcoran - Lemoore|CA311|Kings|06031|P|cc|36.226|-119.5882
CA|311|HNX|Hanford - Corcoran - Lemoore|CA311|Tulare|06107|P|cc|36.226|-119.5882
CA|312|HNX|Visalia - Porterville - Reedley|CA312|Fresno|06019|P|cc|36.3626|-119.2605
CA|312|HNX|Visalia - Porterville - Reedley|CA312|Tulare|06107|P|cc|36.3626|-119.2605
CA|313|HNX|Buena Vista|CA313|Kern|06029|P|cc|35.2078|-119.4499
CA|314|HNX|Bakersfield|CA314|Kern|06029|P|cc|35.3612|-119.0216
CA|315|HNX|Southeast San Joaquin Valley|CA315|Kern|06029|P|cc|35.7755|-119.0391
CA|315|HNX|Southeast San Joaquin Valley|CA315|Tulare|06107|P|cc|35.7755|-119.0391
CA|316|HNX|South End San Joaquin Valley|CA316|Kern|06029|P|cc|35.1382|-118.9898
CA|317|HNX|Mariposa Madera Foothills|CA317|Madera|06039|P|cc|37.3511|-119.9965
CA|317|HNX|Mariposa Madera Foothills|CA317|Mariposa|06043|P|cc|37.3511|-119.9965
CA|317|HNX|Mariposa Madera Foothills|CA317|Merced|06047|P|cc|37.3511|-119.9965
CA|318|HNX|Mariposa-Madera Lower Sierra|CA318|Madera|06039|P|cc|37.4854|-119.8078
CA|318|HNX|Mariposa-Madera Lower Sierra|CA318|Mariposa|06043|P|cc|37.4854|-119.8078
CA|319|HNX|Fresno-Tulare Foothills|CA319|Fresno|06019|P|cc|36.607|-119.2012
CA|319|HNX|Fresno-Tulare Foothills|CA319|Tulare|06107|P|cc|36.607|-119.2012
CA|320|HNX|Fresno-Tulare Lower Sierra|CA320|Fresno|06019|P|cc|36.837|-119.1509
CA|320|HNX|Fresno-Tulare Lower Sierra|CA320|Tulare|06107|P|cc|36.837|-119.1509
CA|321|HNX|South End Sierra Foothills|CA321|Kern|06029|P|cc|35.7347|-118.88
CA|321|HNX|South End Sierra Foothills|CA321|Tulare|06107|P|cc|35.7347|-118.88
CA|322|HNX|South End of the Lower Sierra|CA322|Kern|06029|P|cc|35.9436|-118.7513
CA|322|HNX|South End of the Lower Sierra|CA322|Tulare|06107|P|cc|35.9436|-118.7513
CA|323|HNX|Yosemite NP outside of the valley|CA323|Madera|06039|P|cc|37.8529|-119.553
CA|323|HNX|Yosemite NP outside of the valley|CA323|Mariposa|06043|P|cc|37.8529|-119.553
CA|323|HNX|Yosemite NP outside of the valley|CA323|Tuolumne|06109|P|cc|37.8529|-119.553
CA|324|HNX|Yosemite Valley|CA324|Mariposa|06043|P|cc|37.7184|-119.662
CA|325|HNX|San Joaquin River Canyon|CA325|Fresno|06019|P|cc|37.3286|-119.3176
CA|325|HNX|San Joaquin River Canyon|CA325|Madera|06039|P|cc|37.3286|-119.3176
CA|326|HNX|Upper San Joaquin River|CA326|Fresno|06019|P|cc|37.4492|-119.1195
CA|326|HNX|Upper San Joaquin River|CA326|Madera|06039|P|cc|37.4492|-119.1195
CA|327|HNX|Kaiser to Rodgers Ridge|CA327|Fresno|06019|P|cc|37.1044|-119.0287
CA|328|HNX|Kings Canyon NP|CA328|Fresno|06019|P|cc|36.899|-118.5876
CA|328|HNX|Kings Canyon NP|CA328|Tulare|06107|P|cc|36.899|-118.5876
CA|329|HNX|Grant Grove Area|CA329|Fresno|06019|P|cc|36.7902|-118.8599
CA|329|HNX|Grant Grove Area|CA329|Tulare|06107|P|cc|36.7902|-118.8599
CA|330|HNX|Sequoia NP|CA330|Tulare|06107|P|cc|36.5082|-118.575
CA|331|HNX|South End of the Upper Sierra|CA331|Kern|06029|P|cc|36.0209|-118.3399
CA|331|HNX|South End of the Upper Sierra|CA331|Tulare|06107|P|cc|36.0209|-118.3399
CA|332|HNX|Kern River Valley|CA332|Kern|06029|P|cc|35.6428|-118.4122
CA|332|HNX|Kern River Valley|CA332|Tulare|06107|P|cc|35.6428|-118.4122
CA|333|HNX|Piute Walker Basin|CA333|Kern|06029|P|cc|35.4383|-118.4292
CA|334|HNX|Tehachapi|CA334|Kern|06029|P|cc|35.1324|-118.5472
CA|335|HNX|Grapevine|CA335|Kern|06029|P|cc|34.8909|-118.9043
CA|336|HNX|Frazier Mountain Communities|CA336|Kern|06029|P|cc|34.9239|-119.1812
CA|337|HNX|Indian Wells Valley|CA337|Kern|06029|P|cc|35.6195|-117.7591
CA|338|HNX|Mojave Desert Slopes|CA338|Kern|06029|P|cc|35.2364|-118.1893
CA|339|HNX|Mojave Desert|CA339|Kern|06029|P|cc|35.0734|-117.9052
AL|001|HUN|Lauderdale|AL001|Lauderdale|01077|C|nw|34.9015|-87.6544
AL|002|HUN|Colbert|AL002|Colbert|01033|C|nw|34.7005|-87.8049
AL|003|HUN|Franklin|AL003|Franklin|01059|C|nw|34.4417|-87.8438
AL|004|HUN|Lawrence|AL004|Lawrence|01079|C|nw|34.522|-87.311
AL|005|HUN|Limestone|AL005|Limestone|01083|C|nc|34.8101|-86.9813
AL|006|HUN|Madison|AL006|Madison|01089|C|nc|34.7631|-86.5502
AL|007|HUN|Morgan|AL007|Morgan|01103|C|nc|34.4535|-86.8529
AL|008|HUN|Marshall|AL008|Marshall|01095|C|ne|34.3669|-86.3066
AL|009|HUN|Jackson|AL009|Jackson|01071|C|ne|34.7794|-85.9993
AL|010|HUN|DefireKalb|AL010|DeKalb|01049|C|ne|34.4598|-85.8041
AL|016|HUN|Cullman|AL016|Cullman|01043|C|nc|34.132|-86.8676
TN|076|HUN|Moore|TN076|Moore|47127|C|mi|35.2847|-86.3588
TN|096|HUN|Lincoln|TN096|Lincoln|47103|C|mi|35.1405|-86.5889
TN|097|HUN|Franklin|TN097|Franklin|47051|C|mi|35.1549|-86.0922
KS|032|ICT|Russell|KS032|Russell|20167|C|cc|38.9149|-98.7623
KS|033|ICT|Lincoln|KS033|Lincoln|20105|C|cc|39.0454|-98.2078
KS|047|ICT|Barton|KS047|Barton|20009|C|cc|38.479|-98.7565
KS|048|ICT|Ellsworth|KS048|Ellsworth|20053|C|cc|38.6966|-98.2048
KS|049|ICT|Saline|KS049|Saline|20169|C|cc|38.7839|-97.6501
KS|050|ICT|Rice|KS050|Rice|20159|C|cc|38.3471|-98.2011
KS|051|ICT|McPherson|KS051|McPherson|20113|C|cc|38.3916|-97.648
KS|052|ICT|Marion|KS052|Marion|20115|C|cc|38.3588|-97.0969
KS|053|ICT|Chase|KS053|Chase|20017|C|ec|38.302|-96.594
KS|067|ICT|Reno|KS067|Reno|20155|C|sc|37.9529|-98.0861
KS|068|ICT|Harvey|KS068|Harvey|20079|C|sc|38.0432|-97.4274
KS|069|ICT|Butler|KS069|Butler|20015|C|sc|37.7812|-96.8391
KS|070|ICT|Greenwood|KS070|Greenwood|20073|C|se|37.8778|-96.2327
KS|071|ICT|Woodson|KS071|Woodson|20207|C|se|37.8867|-95.7402
KS|072|ICT|Allen|KS072|Allen|20001|C|se|37.8858|-95.3014
KS|082|ICT|Kingman|KS082|Kingman|20095|C|sc|37.5589|-98.1364
KS|083|ICT|Sedgwick|KS083|Sedgwick|20173|C|sc|37.6848|-97.4611
KS|091|ICT|Harper|KS091|Harper|20077|C|sc|37.1916|-98.0755
KS|092|ICT|Sumner|KS092|Sumner|20191|C|sc|37.2373|-97.4765
KS|093|ICT|Cowley|KS093|Cowley|20035|C|sc|37.2377|-96.8375
KS|094|ICT|Elk|KS094|Elk|20049|C|se|37.4537|-96.2441
KS|095|ICT|Wilson|KS095|Wilson|20205|C|se|37.5593|-95.7434
KS|096|ICT|Neosho|KS096|Neosho|20133|C|se|37.5586|-95.3068
KS|098|ICT|Chautauqua|KS098|Chautauqua|20019|C|se|37.1501|-96.2453
KS|099|ICT|Montgomery|KS099|Montgomery|20125|C|se|37.1925|-95.7429
KS|100|ICT|Labette|KS100|Labette|20099|C|se|37.1913|-95.2976
NC|087|ILM|Robeson|NC087|Robeson|37155|E|se|34.6401|-79.1035
NC|096|ILM|Bladen|NC096|Bladen|37017|E|se|34.6143|-78.5632
NC|099|ILM|Columbus|NC099|Columbus|37047|E|se|34.2655|-78.655
NC|105|ILM|Inland Pender|NC105|Pender|37141|E|se|34.5328|-77.9208
NC|106|ILM|Coastal Pender|NC106|Pender|37141|E|se|34.3814|-77.6465
NC|107|ILM|Inland New Hanover|NC107|New Hanover|37129|E|se|34.2817|-77.8983
NC|108|ILM|Coastal New Hanover|NC108|New Hanover|37129|E|aw|34.1372|-77.8612
NC|108|ILM|Coastal New Hanover|NC108|New Hanover|37129|E|se|34.1372|-77.8612
NC|109|ILM|Inland Brunswick|NC109|Brunswick|37019|E|se|34.1066|-78.2492
NC|110|ILM|Coastal Brunswick|NC110|Brunswick|37019|E|se|33.9367|-78.2222
NC|110|ILM|Coastal Brunswick|NC110|Brunswick|37019|E|se|33.9529|-77.9712
SC|017|ILM|Marlboro|SC017|Marlboro|45069|E|ne|34.602|-79.6786
SC|023|ILM|Darlington|SC023|Darlington|45031|E|ne|34.3324|-79.9577
SC|024|ILM|Dillon|SC024|Dillon|45033|E|ne|34.3915|-79.3789
SC|032|ILM|Florence|SC032|Florence|45041|E|ne|34.0245|-79.7028
SC|033|ILM|Marion|SC033|Marion|45067|E|ne|34.0801|-79.3625
SC|039|ILM|Williamsburg|SC039|Williamsburg|45089|E|ne|33.6199|-79.7277
SC|054|ILM|Coastal Horry|SC054|Horry|45051|E|ne|33.7383|-78.8597
SC|055|ILM|Inland Georgetown|SC055|Georgetown|45043|E|ne|33.4918|-79.3913
SC|056|ILM|Coastal Georgetown|SC056|Georgetown|45043|E|ne|33.3522|-79.2437
SC|058|ILM|Central Horry|SC058|Horry|45051|E|ne|33.8439|-79.0138
SC|059|ILM|Northern Horry|SC059|Horry|45051|E|ne|34.0737|-79.0299
IN|050|ILN|Wayne|IN050|Wayne|18177|E|ec|39.8644|-85.0099
IN|058|ILN|Fayette|IN058|Fayette|18041|E|ec|39.6401|-85.1787
IN|059|ILN|Union|IN059|Union|18161|E|ec|39.6255|-84.9251
IN|066|ILN|Franklin|IN066|Franklin|18047|E|se|39.4148|-85.0603
IN|073|ILN|Ripley|IN073|Ripley|18137|E|se|39.1034|-85.2624
IN|074|ILN|Dearborn|IN074|Dearborn|18029|E|se|39.1453|-84.9733
IN|075|ILN|Ohio|IN075|Ohio|18115|E|se|38.9501|-84.965
IN|080|ILN|Switzerland|IN080|Switzerland|18155|E|se|38.8262|-85.037
KY|089|ILN|Carroll|KY089|Carroll|21041|E|nn|38.6679|-85.1235
KY|090|ILN|Gallatin|KY090|Gallatin|21077|E|nn|38.7569|-84.8592
KY|091|ILN|Boone|KY091|Boone|21015|E|nn|38.97|-84.7279
KY|092|ILN|Kenton|KY092|Kenton|21117|E|nn|38.9333|-84.5331
KY|093|ILN|Campbell|KY093|Campbell|21037|E|nn|38.9465|-84.3793
KY|094|ILN|Owen|KY094|Owen|21187|E|nn|38.5197|-84.828
KY|095|ILN|Grant|KY095|Grant|21081|E|nn|38.6488|-84.6245
KY|096|ILN|Pendleton|KY096|Pendleton|21191|E|nn|38.6957|-84.3602
KY|097|ILN|Bracken|KY097|Bracken|21023|E|nn|38.6888|-84.0901
KY|098|ILN|Robertson|KY098|Robertson|21201|E|nn|38.5188|-84.0521
KY|099|ILN|Mason|KY099|Mason|21161|E|nn|38.5952|-83.824
KY|100|ILN|Lewis|KY100|Lewis|21135|E|ne|38.5317|-83.3781
OH|026|ILN|Hardin|OH026|Hardin|39065|E|wc|40.6615|-83.6594
OH|034|ILN|Mercer|OH034|Mercer|39107|E|wc|40.54|-84.6293
OH|035|ILN|Auglaize|OH035|Auglaize|39011|E|wc|40.5609|-84.2217
OH|042|ILN|Darke|OH042|Darke|39037|E|wc|40.1333|-84.6193
OH|043|ILN|Shelby|OH043|Shelby|39149|E|wc|40.3316|-84.2048
OH|044|ILN|Logan|OH044|Logan|39091|E|wc|40.3885|-83.7658
OH|045|ILN|Union|OH045|Union|39159|E|cc|40.2995|-83.3715
OH|046|ILN|Delaware|OH046|Delaware|39041|E|cc|40.2785|-83.0052
OH|051|ILN|Miami|OH051|Miami|39109|E|wc|40.0534|-84.2289
OH|052|ILN|Champaign|OH052|Champaign|39021|E|wc|40.1378|-83.7696
OH|053|ILN|Clark|OH053|Clark|39023|E|wc|39.9168|-83.7835
OH|054|ILN|Madison|OH054|Madison|39097|E|cc|39.8942|-83.3999
OH|055|ILN|Franklin|OH055|Franklin|39049|E|cc|39.9696|-83.0093
OH|056|ILN|Licking|OH056|Licking|39089|E|cc|40.0918|-82.4835
OH|060|ILN|Preble|OH060|Preble|39135|E|wc|39.7416|-84.6481
OH|061|ILN|Montgomery|OH061|Montgomery|39113|E|wc|39.7545|-84.2906
OH|062|ILN|Greene|OH062|Greene|39057|E|wc|39.6915|-83.8898
OH|063|ILN|Fayette|OH063|Fayette|39047|E|cc|39.5599|-83.4561
OH|064|ILN|Pickaway|OH064|Pickaway|39129|E|cc|39.642|-83.0243
OH|065|ILN|Fairfield|OH065|Fairfield|39045|E|cc|39.7516|-82.6305
OH|070|ILN|Butler|OH070|Butler|39017|E|sw|39.4386|-84.5755
OH|071|ILN|Warren|OH071|Warren|39165|E|sw|39.4277|-84.1668
OH|072|ILN|Clinton|OH072|Clinton|39027|E|sw|39.415|-83.8084
OH|073|ILN|Ross|OH073|Ross|39141|E|sw|39.3376|-83.057
OH|074|ILN|Hocking|OH074|Hocking|39073|E|cc|39.497|-82.4791
OH|077|ILN|Hamilton|OH077|Hamilton|39061|E|sw|39.1954|-84.5426
OH|078|ILN|Clermont|OH078|Clermont|39025|E|sw|39.0476|-84.1522
OH|079|ILN|Brown|OH079|Brown|39015|E|sw|38.9344|-83.868
OH|080|ILN|Highland|OH080|Highland|39071|E|sw|39.1848|-83.6009
OH|081|ILN|Adams|OH081|Adams|39001|E|sw|38.8457|-83.472
OH|082|ILN|Pike|OH082|Pike|39131|E|sw|39.0774|-83.0668
OH|088|ILN|Scioto|OH088|Scioto|39145|E|sw|38.804|-82.9928
IL|027|ILX|Knox|IL027|Knox|17095|C|wc|40.9318|-90.2133
IL|028|ILX|Stark|IL028|Stark|17175|C|nc|41.0934|-89.7975
IL|029|ILX|Peoria|IL029|Peoria|17143|C|cc|40.7881|-89.76
IL|030|ILX|Marshall|IL030|Marshall|17123|C|cc|41.0332|-89.3448
IL|031|ILX|Woodford|IL031|Woodford|17203|C|cc|40.7882|-89.2111
IL|036|ILX|Fulton|IL036|Fulton|17057|C|wc|40.4728|-90.2075
IL|037|ILX|Tazewell|IL037|Tazewell|17179|C|cc|40.5075|-89.5135
IL|038|ILX|McLean|IL038|McLean|17113|C|cc|40.4908|-88.8473
IL|040|ILX|Schuyler|IL040|Schuyler|17169|C|wc|40.158|-90.6151
IL|041|ILX|Mason|IL041|Mason|17125|C|cc|40.2397|-89.9168
IL|042|ILX|Logan|IL042|Logan|17107|C|cc|40.1245|-89.3676
IL|043|ILX|De Witt|IL043|De Witt|17039|C|cc|40.1746|-88.9041
IL|044|ILX|Piatt|IL044|Piatt|17147|C|cc|40.0104|-88.5911
IL|045|ILX|Champaign|IL045|Champaign|17019|C|ec|40.1401|-88.1991
IL|046|ILX|Vermilion|IL046|Vermilion|17183|C|ec|40.1836|-87.7329
IL|047|ILX|Cass|IL047|Cass|17017|C|wc|39.9736|-90.2474
IL|048|ILX|Menard|IL048|Menard|17129|C|cc|40.0274|-89.8022
IL|049|ILX|Scott|IL049|Scott|17171|C|wc|39.6442|-90.4747
IL|050|ILX|Morgan|IL050|Morgan|17137|C|wc|39.7156|-90.2015
IL|051|ILX|Sangamon|IL051|Sangamon|17167|C|cc|39.7582|-89.6589
IL|052|ILX|Christian|IL052|Christian|17021|C|cc|39.5458|-89.2773
IL|053|ILX|Macon|IL053|Macon|17115|C|cc|39.8599|-88.9617
IL|054|ILX|Moultrie|IL054|Moultrie|17139|C|cc|39.6414|-88.6194
IL|055|ILX|Douglas|IL055|Douglas|17041|C|ec|39.7695|-88.2174
IL|056|ILX|Coles|IL056|Coles|17029|C|ec|39.5202|-88.2218
IL|057|ILX|Edgar|IL057|Edgar|17045|C|ec|39.6786|-87.7456
IL|061|ILX|Shelby|IL061|Shelby|17173|C|cc|39.3911|-88.8055
IL|062|ILX|Cumberland|IL062|Cumberland|17035|C|ec|39.2732|-88.2402
IL|063|ILX|Clark|IL063|Clark|17023|C|ec|39.3335|-87.7878
IL|066|ILX|Effingham|IL066|Effingham|17049|C|sc|39.0597|-88.5899
IL|067|ILX|Jasper|IL067|Jasper|17079|C|se|39.01|-88.1538
IL|068|ILX|Crawford|IL068|Crawford|17033|C|ec|39.0028|-87.7595
IL|071|ILX|Clay|IL071|Clay|17025|C|sc|38.7542|-88.4902
IL|072|ILX|Richland|IL072|Richland|17159|C|se|38.7124|-88.085
IL|073|ILX|Lawrence|IL073|Lawrence|17101|C|se|38.72|-87.7266
IN|021|IND|Carroll|IN021|Carroll|18015|E|nc|40.5828|-86.5635
IN|028|IND|Warren|IN028|Warren|18171|E|wc|40.3469|-87.3533
IN|029|IND|Tippecanoe|IN029|Tippecanoe|18157|E|wc|40.3886|-86.8941
IN|030|IND|Clinton|IN030|Clinton|18023|E|cc|40.3017|-86.4752
IN|031|IND|Howard|IN031|Howard|18067|E|cc|40.4836|-86.1169
IN|035|IND|Fountain|IN035|Fountain|18045|E|wc|40.1209|-87.2419
IN|036|IND|Montgomery|IN036|Montgomery|18107|E|wc|40.0404|-86.8933
IN|037|IND|Boone|IN037|Boone|18011|E|cc|40.0508|-86.4687
IN|038|IND|Tipton|IN038|Tipton|18159|E|cc|40.3114|-86.0519
IN|039|IND|Hamilton|IN039|Hamilton|18057|E|cc|40.0725|-86.052
IN|040|IND|Madison|IN040|Madison|18095|E|cc|40.1616|-85.7194
IN|041|IND|Delaware|IN041|Delaware|18035|E|ec|40.2276|-85.3969
IN|042|IND|Randolph|IN042|Randolph|18135|E|ec|40.1576|-85.0114
IN|043|IND|Vermillion|IN043|Vermillion|18165|E|wc|39.8538|-87.464
IN|044|IND|Parke|IN044|Parke|18121|E|wc|39.7736|-87.2063
IN|045|IND|Putnam|IN045|Putnam|18133|E|wc|39.6663|-86.845
IN|046|IND|Hendricks|IN046|Hendricks|18063|E|cc|39.7695|-86.51
IN|047|IND|Marion|IN047|Marion|18097|E|cc|39.7816|-86.1384
IN|048|IND|Hancock|IN048|Hancock|18059|E|cc|39.8235|-85.7732
IN|049|IND|Henry|IN049|Henry|18065|E|ec|39.9311|-85.3965
IN|051|IND|Vigo|IN051|Vigo|18167|E|wc|39.4306|-87.39
IN|052|IND|Clay|IN052|Clay|18021|E|wc|39.3928|-87.1158
IN|053|IND|Owen|IN053|Owen|18119|E|wc|39.3129|-86.8376
IN|054|IND|Morgan|IN054|Morgan|18109|E|cc|39.4815|-86.4462
IN|055|IND|Johnson|IN055|Johnson|18081|E|cc|39.4899|-86.1017
IN|056|IND|Shelby|IN056|Shelby|18145|E|cc|39.5236|-85.7918
IN|057|IND|Rush|IN057|Rush|18139|E|cc|39.6199|-85.4657
IN|060|IND|Sullivan|IN060|Sullivan|18153|E|sw|39.0888|-87.4146
IN|061|IND|Greene|IN061|Greene|18055|E|sw|39.0363|-86.962
IN|062|IND|Monroe|IN062|Monroe|18105|E|sc|39.1609|-86.5231
IN|063|IND|Brown|IN063|Brown|18013|E|sc|39.1962|-86.2274
IN|064|IND|Bartholomew|IN064|Bartholomew|18005|E|cc|39.2059|-85.8977
IN|065|IND|Decatur|IN065|Decatur|18031|E|cc|39.3069|-85.5013
IN|067|IND|Knox|IN067|Knox|18083|E|sw|38.6891|-87.418
IN|068|IND|Daviess|IN068|Daviess|18027|E|sw|38.7024|-87.0721
IN|069|IND|Martin|IN069|Martin|18101|E|sw|38.708|-86.8031
IN|070|IND|Lawrence|IN070|Lawrence|18093|E|sc|38.8412|-86.4834
IN|071|IND|Jackson|IN071|Jackson|18071|E|sc|38.9064|-86.0376
IN|072|IND|Jennings|IN072|Jennings|18079|E|se|38.9969|-85.6281
IN|005|IWX|Elkhart|IN005|Elkhart|18039|E|nc|41.5974|-85.8587
IN|006|IWX|Lagrange|IN006|Lagrange|18087|E|ne|41.6427|-85.4265
IN|007|IWX|Steuben|IN007|Steuben|18151|E|ne|41.6439|-85.0008
IN|008|IWX|Noble|IN008|Noble|18113|E|ne|41.3986|-85.4174
IN|009|IWX|De Kalb|IN009|De Kalb|18033|E|ne|41.3976|-84.9991
IN|012|IWX|Starke|IN012|Starke|18149|C|nw|41.281|-86.6478
IN|013|IWX|Pulaski|IN013|Pulaski|18131|C|nw|41.0419|-86.6989
IN|014|IWX|Marshall|IN014|Marshall|18099|E|nc|41.325|-86.2618
IN|015|IWX|Fulton|IN015|Fulton|18049|E|nc|41.047|-86.2636
IN|017|IWX|Whitley|IN017|Whitley|18183|E|ne|41.1394|-85.5052
IN|018|IWX|Allen|IN018|Allen|18003|E|ne|41.0908|-85.0665
IN|020|IWX|White|IN020|White|18181|E|nw|40.7499|-86.8654
IN|022|IWX|Cass|IN022|Cass|18017|E|nc|40.7615|-86.346
IN|023|IWX|Miami|IN023|Miami|18103|E|nc|40.7695|-86.0451
IN|024|IWX|Wabash|IN024|Wabash|18169|E|nc|40.8457|-85.794
IN|025|IWX|Huntington|IN025|Huntington|18069|E|ne|40.8292|-85.4881
IN|026|IWX|Wells|IN026|Wells|18179|E|ne|40.7291|-85.2212
IN|027|IWX|Adams|IN027|Adams|18001|E|ne|40.7455|-84.9366
IN|032|IWX|Grant|IN032|Grant|18053|E|cc|40.5158|-85.6548
IN|033|IWX|Blackford|IN033|Blackford|18009|E|ec|40.4735|-85.3248
IN|034|IWX|Jay|IN034|Jay|18075|E|ec|40.438|-85.0057
IN|103|IWX|Northern La Porte|IN103|La Porte|18091|C|nw|41.6261|-86.7063
IN|104|IWX|Eastern St. Joseph|IN104|St. Joseph|18141|E|nc|41.6193|-86.2095
IN|116|IWX|Northern Kosciusko|IN116|Kosciusko|18085|E|nc|41.3378|-85.8378
IN|203|IWX|Southern La Porte|IN203|La Porte|18091|C|nw|41.4091|-86.7975
IN|204|IWX|Western St. Joseph|IN204|St. Joseph|18141|E|nc|41.6119|-86.4382
IN|216|IWX|Southern Kosciusko|IN216|Kosciusko|18085|E|nc|41.1497|-85.8838
MI|078|IWX|Cass|MI078|Cass|26027|E|sw|41.9153|-85.9936
MI|079|IWX|St. Joseph|MI079|St. Joseph|26149|E|sw|41.9145|-85.5278
MI|080|IWX|Branch|MI080|Branch|26023|E|sw|41.9161|-85.059
MI|081|IWX|Hillsdale|MI081|Hillsdale|26059|E|se|41.8878|-84.593
MI|177|IWX|Northern Berrien|MI177|Berrien|26021|E|sw|42.1472|-86.3368
MI|277|IWX|Southern Berrien|MI277|Berrien|26021|E|sw|41.8971|-86.4348
OH|001|IWX|Williams|OH001|Williams|39171|E|nw|41.5603|-84.5882
OH|002|IWX|Fulton|OH002|Fulton|39051|E|nw|41.6018|-84.1301
OH|004|IWX|Defiance|OH004|Defiance|39039|E|nw|41.324|-84.4906
OH|005|IWX|Henry|OH005|Henry|39069|E|nw|41.3339|-84.0682
OH|015|IWX|Paulding|OH015|Paulding|39125|E|wc|41.1166|-84.5801
OH|016|IWX|Putnam|OH016|Putnam|39137|E|wc|41.0221|-84.1317
OH|024|IWX|Van Wert|OH024|Van Wert|39161|E|wc|40.8554|-84.5861
OH|025|IWX|Allen|OH025|Allen|39003|E|wc|40.7715|-84.1057
AR|074|JAN|Ashley|AR074|Ashley|05003|C|se|33.1912|-91.7679
AR|075|JAN|Chicot|AR075|Chicot|05017|C|se|33.2672|-91.294
LA|007|JAN|Morehouse|LA007|Morehouse|22067|C|ne|32.8205|-91.8017
LA|008|JAN|West Carroll|LA008|West Carroll|22123|C|ne|32.7885|-91.4567
LA|009|JAN|East Carroll|LA009|East Carroll|22035|C|ne|32.7326|-91.2351
LA|015|JAN|Richland|LA015|Richland|22083|C|ne|32.4177|-91.7636
LA|016|JAN|Madison|LA016|Madison|22065|C|ne|32.3643|-91.2427
LA|023|JAN|Franklin|LA023|Franklin|22041|C|ne|32.1332|-91.6738
LA|024|JAN|Catahoula|LA024|Catahoula|22025|C|ne|31.6661|-91.8471
LA|025|JAN|Tensas|LA025|Tensas|22107|C|ne|32.0017|-91.34
LA|026|JAN|Concordia|LA026|Concordia|22029|C|ne|31.4458|-91.6397
MS|018|JAN|Bolivar|MS018|Bolivar|28011|C|nw|33.7955|-90.8804
MS|019|JAN|Sunflower|MS019|Sunflower|28133|C|nw|33.6023|-90.5887
MS|025|JAN|Leflore|MS025|Leflore|28083|C|nc|33.5505|-90.301
MS|026|JAN|Grenada|MS026|Grenada|28043|C|nc|33.77|-89.802
MS|027|JAN|Carroll|MS027|Carroll|28015|C|nc|33.4485|-89.9202
MS|028|JAN|Montgomery|MS028|Montgomery|28097|C|nc|33.4941|-89.6164
MS|029|JAN|Webster|MS029|Webster|28155|C|nc|33.6131|-89.2848
MS|030|JAN|Clay|MS030|Clay|28025|C|ne|33.6557|-88.7815
MS|031|JAN|Lowndes|MS031|Lowndes|28087|C|ne|33.4729|-88.4433
MS|032|JAN|Choctaw|MS032|Choctaw|28019|C|cc|33.3473|-89.2484
MS|033|JAN|Oktibbeha|MS033|Oktibbeha|28105|C|ne|33.425|-88.8793
MS|034|JAN|Washington|MS034|Washington|28151|C|nw|33.2836|-90.9474
MS|035|JAN|Humphreys|MS035|Humphreys|28053|C|cc|33.1287|-90.5265
MS|036|JAN|Holmes|MS036|Holmes|28051|C|cc|33.1235|-90.0921
MS|037|JAN|Attala|MS037|Attala|28007|C|cc|33.0863|-89.5817
MS|038|JAN|Winston|MS038|Winston|28159|C|ec|33.0885|-89.0344
MS|039|JAN|Noxubee|MS039|Noxubee|28103|C|ec|33.1101|-88.5698
MS|040|JAN|Issaquena|MS040|Issaquena|28055|C|wc|32.7414|-90.9892
MS|041|JAN|Sharkey|MS041|Sharkey|28125|C|wc|32.8797|-90.8132
MS|042|JAN|Yazoo|MS042|Yazoo|28163|C|cc|32.7804|-90.3965
MS|043|JAN|Madison|MS043|Madison|28089|C|cc|32.6347|-90.0338
MS|044|JAN|Leake|MS044|Leake|28079|C|cc|32.7535|-89.5241
MS|045|JAN|Neshoba|MS045|Neshoba|28099|C|ec|32.7535|-89.1176
MS|046|JAN|Kemper|MS046|Kemper|28069|C|ec|32.7546|-88.6412
MS|047|JAN|Warren|MS047|Warren|28149|C|wc|32.3574|-90.8521
MS|048|JAN|Hinds|MS048|Hinds|28049|C|cc|32.2667|-90.4427
MS|049|JAN|Rankin|MS049|Rankin|28121|C|cc|32.2641|-89.9457
MS|050|JAN|Scott|MS050|Scott|28123|C|cc|32.4064|-89.5376
MS|051|JAN|Newton|MS051|Newton|28101|C|ec|32.4002|-89.1188
MS|052|JAN|Lauderdale|MS052|Lauderdale|28075|C|ec|32.4043|-88.6626
MS|053|JAN|Claiborne|MS053|Claiborne|28021|C|sw|31.9737|-90.9118
MS|054|JAN|Copiah|MS054|Copiah|28029|C|cc|31.8692|-90.4488
MS|055|JAN|Simpson|MS055|Simpson|28127|C|cc|31.9132|-89.9195
MS|056|JAN|Smith|MS056|Smith|28129|C|cc|32.0177|-89.5067
MS|057|JAN|Jasper|MS057|Jasper|28061|C|ec|32.0191|-89.1188
MS|058|JAN|Clarke|MS058|Clarke|28023|C|ec|32.0414|-88.6894
MS|059|JAN|Jefferson|MS059|Jefferson|28063|C|sw|31.7342|-91.0371
MS|060|JAN|Adams|MS060|Adams|28001|C|sw|31.4832|-91.3531
MS|061|JAN|Franklin|MS061|Franklin|28037|C|sw|31.4772|-90.8978
MS|062|JAN|Lincoln|MS062|Lincoln|28085|C|sc|31.5324|-90.454
MS|063|JAN|Lawrence|MS063|Lawrence|28077|C|sc|31.5502|-90.107
MS|064|JAN|Jefferson Davis|MS064|Jefferson Davis|28065|C|sc|31.5696|-89.823
MS|065|JAN|Covington|MS065|Covington|28031|C|se|31.6332|-89.5526
MS|066|JAN|Jones|MS066|Jones|28067|C|se|31.6226|-89.1688
MS|072|JAN|Marion|MS072|Marion|28091|C|sc|31.2308|-89.8224
MS|073|JAN|Lamar|MS073|Lamar|28073|C|se|31.2059|-89.5087
MS|074|JAN|Forrest|MS074|Forrest|28035|C|se|31.1889|-89.2579
FL|120|JAX|Eastern Hamilton|FL120|Hamilton|12047|E|nn|30.4942|-82.8552
FL|220|JAX|Western Hamilton|FL220|Hamilton|12047|E|nn|30.5003|-83.1184
FL|021|JAX|Suwannee|FL021|Suwannee|12121|E|nn|30.1956|-82.9915
FL|023|JAX|Baker|FL023|Baker|12003|E|ne|30.331|-82.2846
FL|024|JAX|Inland Nassau|FL024|Nassau|12089|E|ne|30.6095|-81.8085
FL|030|JAX|Union|FL030|Union|12125|E|nn|30.0439|-82.3714
FL|031|JAX|Bradford|FL031|Bradford|12007|E|nn|29.9502|-82.1689
FL|033|JAX|Inland St. Johns|FL033|St. Johns|12109|E|ne|29.8671|-81.4979
FL|035|JAX|Gilchrist|FL035|Gilchrist|12041|E|nn|29.7259|-82.8005
FL|038|JAX|Inland Flagler|FL038|Flagler|12035|E|ne|29.4499|-81.3306
FL|124|JAX|Coastal Nassau|FL124|Nassau|12089|E|ne|30.6095|-81.8085
FL|125|JAX|Coastal Duval|FL125|Duval|12031|E|ne|30.352|-81.5262
FL|132|JAX|Eastern Clay|FL132|Clay|12019|E|ne|30.0117|-81.6792
FL|133|JAX|Coastal St. Johns|FL133|St. Johns|12109|E|ne|29.9525|-81.3629
FL|136|JAX|Eastern Alachua |FL136|Alachua|12001|E|nn|29.6896|-82.2664
FL|137|JAX|Eastern Putnam|FL137|Putnam|12107|E|ne|29.5498|-81.612
FL|138|JAX|Coastal Flagler|FL138|Flagler|12035|E|ne|29.5436|-81.1875
FL|140|JAX|Eastern Marion |FL140|Marion|12083|E|nn|29.217|-81.7957
FL|225|JAX|Trout River|FL225|Duval|12031|E|ne|30.4129|-81.7184
FL|232|JAX|Western Clay|FL232|Clay|12019|E|ne|29.9783|-81.8881
FL|236|JAX|Western Alachua |FL236|Alachua|12001|E|nn|29.6482|-82.523
FL|237|JAX|Western Putnam|FL237|Putnam|12107|E|ne|29.6558|-81.8502
FL|240|JAX|Central Marion |FL240|Marion|12083|E|nn|29.2233|-82.0497
FL|325|JAX|South Central Duval|FL325|Duval|12031|E|ne|30.2148|-81.6487
FL|340|JAX|Western Marion |FL340|Marion|12083|E|nn|29.1889|-82.3279
FL|425|JAX|Western Duval|FL425|Duval|12031|E|ne|30.3364|-81.8388
GA|132|JAX|Coffee|GA132|Coffee|13069|E|se|31.5492|-82.8493
GA|133|JAX|Jeff Davis|GA133|Jeff Davis|13161|E|se|31.8056|-82.637
GA|134|JAX|Bacon|GA134|Bacon|13005|E|se|31.5537|-82.4527
GA|135|JAX|Appling|GA135|Appling|13001|E|se|31.7493|-82.289
GA|136|JAX|Wayne|GA136|Wayne|13305|E|se|31.5515|-81.9168
GA|149|JAX|Atkinson|GA149|Atkinson|13003|E|se|31.2971|-82.88
GA|151|JAX|Pierce|GA151|Pierce|13229|E|se|31.3589|-82.2133
GA|152|JAX|Brantley|GA152|Brantley|13025|E|se|31.197|-81.9819
GA|153|JAX|Inland Glynn|GA153|Glynn|13127|E|se|31.2698|-81.639
GA|154|JAX|Coastal Glynn|GA154|Glynn|13127|E|se|31.1999|-81.4405
GA|162|JAX|Echols|GA162|Echols|13101|E|se|30.7101|-82.8939
GA|163|JAX|Clinch|GA163|Clinch|13065|E|se|30.9151|-82.7063
GA|165|JAX|Inland Camden|GA165|Camden|13039|E|se|30.9642|-81.7688
GA|166|JAX|Coastal Camden|GA166|Camden|13039|E|se|30.8884|-81.5544
GA|250|JAX|Northern Ware |GA250|Ware|13299|E|se|31.1996|-82.4623
GA|264|JAX|Northeastern Charlton |GA264|Charlton|13049|E|se|30.947|-81.9942
GA|350|JAX|Southern Ware |GA350|Ware|13299|E|se|30.7473|-82.3431
GA|364|JAX|Western Charlton |GA364|Charlton|13049|E|se|30.7368|-82.1771
KY|044|JKL|Fleming|KY044|Fleming|21069|E|ec|38.3701|-83.6967
KY|050|JKL|Montgomery|KY050|Montgomery|21173|E|ec|38.0336|-83.9132
KY|051|JKL|Bath|KY051|Bath|21011|E|ec|38.1449|-83.7428
KY|052|JKL|Rowan|KY052|Rowan|21205|E|ec|38.1963|-83.4211
KY|058|JKL|Estill|KY058|Estill|21065|E|ec|37.6924|-83.9643
KY|059|JKL|Powell|KY059|Powell|21197|E|ec|37.8312|-83.8239
KY|060|JKL|Menifee|KY060|Menifee|21165|E|ec|37.9414|-83.5989
KY|068|JKL|Rockcastle|KY068|Rockcastle|21203|E|sc|37.3652|-84.316
KY|069|JKL|Jackson|KY069|Jackson|21109|E|se|37.4198|-84.0058
KY|079|JKL|Pulaski|KY079|Pulaski|21199|E|sc|37.1039|-84.5771
KY|080|JKL|Laurel|KY080|Laurel|21125|E|sc|37.1107|-84.1178
KY|083|JKL|Wayne|KY083|Wayne|21231|E|sc|36.8013|-84.8285
KY|084|JKL|McCreary|KY084|McCreary|21147|E|sc|36.7371|-84.4841
KY|085|JKL|Whitley|KY085|Whitley|21235|E|sc|36.7582|-84.1452
KY|086|JKL|Knox|KY086|Knox|21121|E|se|36.8907|-83.8539
KY|087|JKL|Bell|KY087|Bell|21013|E|se|36.7307|-83.674
KY|088|JKL|Harlan|KY088|Harlan|21095|E|se|36.857|-83.2179
KY|104|JKL|Elliott|KY104|Elliott|21063|E|ec|38.1179|-83.0976
KY|106|JKL|Morgan|KY106|Morgan|21175|E|se|37.9223|-83.2589
KY|107|JKL|Johnson|KY107|Johnson|21115|E|ne|37.8467|-82.8314
KY|108|JKL|Wolfe|KY108|Wolfe|21237|E|se|37.7393|-83.4931
KY|109|JKL|Magoffin|KY109|Magoffin|21153|E|se|37.7066|-83.0648
KY|110|JKL|Floyd|KY110|Floyd|21071|E|se|37.5572|-82.7457
KY|111|JKL|Lee|KY111|Lee|21129|E|se|37.5947|-83.7163
KY|112|JKL|Breathitt|KY112|Breathitt|21025|E|se|37.5216|-83.3241
KY|113|JKL|Knott|KY113|Knott|21119|E|se|37.354|-82.954
KY|114|JKL|Owsley|KY114|Owsley|21189|E|se|37.4193|-83.6832
KY|115|JKL|Perry|KY115|Perry|21193|E|se|37.2443|-83.2215
KY|116|JKL|Clay|KY116|Clay|21051|E|se|37.1598|-83.7146
KY|117|JKL|Leslie|KY117|Leslie|21131|E|se|37.0941|-83.3811
KY|118|JKL|Letcher|KY118|Letcher|21133|E|se|37.1212|-82.8553
KY|119|JKL|Martin|KY119|Martin|21159|E|ne|37.8016|-82.5132
KY|120|JKL|Pike|KY120|Pike|21195|E|se|37.469|-82.3958
FL|076|KEY|Monroe Upper Keys|FL076|Upper Keys in Monroe|12087|E|se|25.1472|-80.4195
FL|077|KEY|Monroe Middle Keys|FL077|Middle Keys in Monroe|12087|E|se|24.7471|-80.9876
FL|078|KEY|Monroe Lower Keys|FL078|Lower Keys in Monroe|12087|E||24.6514|-81.5527
NE|004|LBF|Sheridan|NE004|Sheridan|31161|M|pa|42.5048|-102.409
NE|005|LBF|Eastern Cherry|NE005|Cherry|31031|MC|nc|42.5577|-100.5076
NE|006|LBF|Keya Paha|NE006|Keya Paha|31103|C|nc|42.8789|-99.7124
NE|007|LBF|Boyd|NE007|Boyd|31015|C|nc|42.8997|-98.7665
NE|008|LBF|Brown|NE008|Brown|31017|C|nc|42.43|-99.9295
NE|009|LBF|Rock|NE009|Rock|31149|C|nc|42.4213|-99.45
NE|010|LBF|Holt|NE010|Holt|31089|C|nc|42.4557|-98.7838
NE|022|LBF|Garden|NE022|Garden|31069|M|pa|41.6194|-102.3354
NE|023|LBF|Grant|NE023|Grant|31075|M|wc|41.915|-101.7405
NE|024|LBF|Hooker|NE024|Hooker|31091|M|wc|41.9159|-101.1353
NE|025|LBF|Thomas|NE025|Thomas|31171|C|nc|41.9135|-100.5558
NE|026|LBF|Blaine|NE026|Blaine|31009|C|nc|41.9128|-99.9769
NE|027|LBF|Loup|NE027|Loup|31115|C|nc|41.9138|-99.4544
NE|028|LBF|Garfield|NE028|Garfield|31071|C|nc|41.9143|-98.9914
NE|029|LBF|Wheeler|NE029|Wheeler|31183|C|nc|41.9148|-98.5282
NE|035|LBF|Arthur|NE035|Arthur|31005|M|wc|41.5689|-101.6959
NE|036|LBF|McPherson|NE036|McPherson|31117|C|wc|41.5681|-101.0605
NE|037|LBF|Logan|NE037|Logan|31113|C|wc|41.5665|-100.4828
NE|038|LBF|Custer|NE038|Custer|31041|C|cc|41.3943|-99.7261
NE|056|LBF|Deuel|NE056|Deuel|31049|M|pa|41.1116|-102.3339
NE|057|LBF|Keith|NE057|Keith|31101|M|sw|41.1988|-101.6613
NE|058|LBF|Perkins|NE058|Perkins|31135|M|sw|40.8509|-101.6496
NE|059|LBF|Lincoln|NE059|Lincoln|31111|C|sw|41.0478|-100.7452
NE|069|LBF|Chase|NE069|Chase|31029|M|sw|40.5242|-101.6979
NE|070|LBF|Hayes|NE070|Hayes|31085|C|sw|40.5248|-101.0618
NE|071|LBF|Frontier|NE071|Frontier|31063|C|sw|40.5301|-100.3942
NE|094|LBF|Western Cherry|NE094|Cherry|31031|MC|nc|42.5381|-101.4432
LA|027|LCH|Vernon|LA027|Vernon|22115|C|wc|31.1083|-93.1842
LA|028|LCH|Rapides|LA028|Rapides|22079|C|cc|31.1986|-92.5332
LA|029|LCH|Avoyelles|LA029|Avoyelles|22009|C|cc|31.0762|-92.0013
LA|030|LCH|Beauregard|LA030|Beauregard|22011|C|sw|30.6485|-93.3434
LA|031|LCH|Allen|LA031|Allen|22003|C|sw|30.6528|-92.8279
LA|032|LCH|Evangeline|LA032|Evangeline|22039|C|cc|30.729|-92.4059
LA|033|LCH|St. Landry|LA033|St. Landry|22097|C|cc|30.5989|-92.0058
LA|044|LCH|Lafayette|LA044|Lafayette|22055|C|sc|30.2063|-92.0639
LA|045|LCH|Upper St. Martin|LA045|St. Martin|22099|C|sc|30.2282|-91.7267
LA|055|LCH|Lower St. Martin|LA055|St. Martin|22099|C|sc|29.8466|-91.2705
LA|073|LCH|West Cameron|LA073|Cameron|22023|C|sw|29.8677|-93.146
LA|074|LCH|East Cameron|LA074|Cameron|22023|C|sw|29.8677|-93.146
LA|152|LCH|Upper Vermilion|LA152|Vermilion|22113|C|sw|30.0498|-92.2739
LA|141|LCH|Northern Calcasieu|LA141|Calcasieu|22019|C|sw|30.3127|-93.4199
LA|142|LCH|Northern Jefferson Davis|LA142|Jefferson Davis|22053|C|sw|30.3481|-92.8227
LA|143|LCH|Northern Acadia|LA143|Acadia|22001|C|sw|30.3309|-92.4024
LA|153|LCH|Upper Iberia|LA153|Iberia|22045|C|sc|30.0091|-91.6312
LA|154|LCH|Upper St. Mary|LA154|St. Mary|22101|C|sc|29.8162|-91.4287
LA|241|LCH|Southern Calcasieu|LA241|Calcasieu|22019|C|sw|30.1333|-93.2867
LA|242|LCH|Southern Jefferson Davis|LA242|Jefferson Davis|22053|C|sw|30.1392|-92.7996
LA|243|LCH|Southern Acadia|LA243|Acadia|22001|C|sw|30.1309|-92.45
LA|252|LCH|Lower Vermilion|LA252|Vermilion|22113|C|sw|29.7894|-92.3378
LA|253|LCH|Lower Iberia|LA253|Iberia|22045|C|sc|29.7499|-91.8554
LA|254|LCH|Lower St. Mary|LA254|St. Mary|22101|C|sc|29.671|-91.4596
TX|515|LCH|Upper Jefferson|TX515|Jefferson|48245|C|se|30.037|-94.2917
TX|516|LCH|Northern Orange|TX516|Orange|48361|C|se|30.1826|-93.907
TX|615|LCH|Lower Jefferson|TX615|Jefferson|48245|C|se|29.8231|-94.1248
TX|616|LCH|Southern Orange|TX616|Orange|48361|C|se|30.0641|-93.8842
TX|180|LCH|Tyler|TX180|Tyler|48457|C|se|30.7712|-94.3765
TX|201|LCH|Hardin|TX201|Hardin|48199|C|se|30.3324|-94.3903
TX|259|LCH|Northern Jasper|TX259|Jasper|48241|C|se|30.8641|-94.0341
TX|260|LCH|Northern Newton|TX260|Newton|48351|C|se|30.8876|-93.7287
TX|261|LCH|Southern Jasper|TX261|Jasper|48241|C|se|30.3824|-93.9977
TX|262|LCH|Southern Newton|TX262|Newton|48351|C|se|30.383|-93.8089
LA|034|LIX|Pointe Coupee|LA034|Pointe Coupee|22077|C|se|30.7097|-91.6009
LA|035|LIX|West Feliciana|LA035|West Feliciana|22125|C|se|30.8798|-91.42
LA|036|LIX|East Feliciana|LA036|East Feliciana|22037|C|se|30.8451|-91.0455
LA|037|LIX|St. Helena|LA037|St. Helena|22091|C|se|30.822|-90.7103
LA|039|LIX|Washington|LA039|Washington|22117|C|se|30.8534|-90.0405
LA|046|LIX|Iberville|LA046|Iberville|22047|C|se|30.2585|-91.3494
LA|047|LIX|West Baton Rouge|LA047|West Baton Rouge|22121|C|se|30.4634|-91.3134
LA|048|LIX|East Baton Rouge|LA048|East Baton Rouge|22033|C|se|30.5383|-91.0957
LA|056|LIX|Assumption|LA056|Assumption|22007|C|se|29.9006|-91.0626
LA|057|LIX|St. James|LA057|St. James|22093|C|se|30.0263|-90.7962
LA|058|LIX|St. John The Baptist|LA058|St. John The Baptist|22095|C|se|30.0792|-90.5462
LA|059|LIX|Upper Lafourche|LA059|Lafourche|22057|C|se|29.7251|-90.5707
LA|060|LIX|St. Charles|LA060|St. Charles|22089|C|se|29.8836|-90.363
LA|064|LIX|Upper St. Bernard|LA064|St. Bernard|22087|C|se|29.913|-89.874
LA|065|LIX|Upper Terrebonne|LA065|Terrebonne|22109|C|se|29.639|-90.8383
LA|066|LIX|Lower Terrebonne|LA066|Terrebonne|22109|C|se|29.3727|-90.8628
LA|067|LIX|Lower Lafourche|LA067|Lafourche|22057|C|se|29.3739|-90.2534
LA|068|LIX|Coastal Jefferson|LA068|Jefferson|22051|C|se|29.5064|-90.0566
LA|069|LIX|Lower Plaquemines|LA069|Plaquemines|22075|C|se|29.4206|-89.6038
LA|070|LIX|Lower St. Bernard|LA070|St. Bernard|22087|C|se|29.8488|-89.5466
LA|071|LIX|Northern Tangipahoa|LA071|Tangipahoa|22105|C|se|30.8274|-90.4379
LA|076|LIX|Southeast St. Tammany|LA076|St. Tammany|22103|C|se|30.2377|-89.7162
LA|077|LIX|Western Orleans|LA077|Orleans|22071|C|se|29.9827|-90.0257
LA|078|LIX|Eastern Orleans|LA078|Orleans|22071|C|se|30.0867|-89.7981
LA|079|LIX|Northern St. Tammany|LA079|St. Tammany|22103|C|se|30.5081|-89.9603
LA|080|LIX|Southwestern St. Tammany|LA080|St. Tammany|22103|C|se|30.3605|-90.0385
LA|081|LIX|Central Tangipahoa|LA081|Tangipahoa|22105|C|se|30.5718|-90.4031
LA|082|LIX|Lower Tangipahoa|LA082|Tangipahoa|22105|C|se|30.3899|-90.372
LA|083|LIX|Northern Livingston|LA083|Livingston|22063|C|se|30.505|-90.7744
LA|084|LIX|Southern Livingston|LA084|Livingston|22063|C|se|30.3135|-90.6508
LA|085|LIX|Western Ascension|LA085|Ascension|22005|C|se|30.207|-90.9623
LA|086|LIX|Eastern Ascension|LA086|Ascension|22005|C|se|30.1944|-90.7769
LA|087|LIX|Upper Jefferson|LA087|Jefferson|22051|C|se|29.9317|-90.1645
LA|088|LIX|Lower Jefferson|LA088|Jefferson|22051|C|se|29.7222|-90.1222
LA|089|LIX|Upper Plaquemines|LA089|Plaquemines|22075|C|se|29.8465|-90.0107
LA|090|LIX|Central Plaquemines|LA090|Plaquemines|22075|C|se|29.7668|-89.9679
MS|068|LIX|Wilkinson|MS068|Wilkinson|28157|C|ss|31.161|-91.3109
MS|069|LIX|Amite|MS069|Amite|28005|C|ss|31.1744|-90.8045
MS|070|LIX|Pike|MS070|Pike|28113|C|ss|31.1749|-90.4042
MS|071|LIX|Walthall|MS071|Walthall|28147|C|ss|31.1485|-90.1061
MS|077|LIX|Pearl River|MS077|Pearl River|28109|C|ss|30.7686|-89.5898
MS|083|LIX|Northern Hancock|MS083|Hancock|28045|C|ss|30.5171|-89.4768
MS|084|LIX|Northern Harrison|MS084|Harrison|28047|C|ss|30.5627|-89.1206
MS|085|LIX|Northern Jackson|MS085|Jackson|28059|C|ss|30.6348|-88.6549
MS|086|LIX|Southern Hancock|MS086|Hancock|28045|C|ss|30.4164|-89.4887
MS|087|LIX|Southern Harrison|MS087|Harrison|28047|C|ss|30.4062|-89.1138
MS|088|LIX|Southern Jackson|MS088|Jackson|28059|C|ss|30.4468|-88.6154
NV|030|LKN|Humboldt County|NV030|Humboldt|32013|P|nw|41.4068|-118.112
NV|031|LKN|Northern Elko County|NV031|Elko|32007|P|ne|41.5447|-115.5974
NV|033|LKN|Extreme Eastern Elko County|NV033|Elko|32007|P|ne|40.6482|-114.2331
NV|034|LKN|Ruby Mountains/East Humboldt Range|NV034|Elko|32007|P|ne|40.544|-115.3911
NV|034|LKN|Ruby Mountains/East Humboldt Range|NV034|White Pine|32033|P|ee|40.544|-115.3911
NV|035|LKN|White Pine County|NV035|White Pine|32033|P|ee|39.4383|-114.8977
NV|036|LKN|Northern Lander County and Northern Eureka County|NV036|Eureka|32011|P|nc|40.4898|-116.7009
NV|036|LKN|Northern Lander County and Northern Eureka County|NV036|Lander|32015|P|nc|40.4898|-116.7009
NV|037|LKN|Southern Lander County and Southern Eureka County|NV037|Eureka|32011|P|nc|39.6135|-116.7096
NV|037|LKN|Southern Lander County and Southern Eureka County|NV037|Lander|32015|P|nc|39.6135|-116.7096
NV|038|LKN|Southwest Elko County|NV038|Elko|32007|P|ne|40.7184|-115.7303
NV|039|LKN|South Central Elko County|NV039|Elko|32007|P|ne|40.5796|-114.8566
NV|040|LKN|Northwestern Nye County|NV040|Nye|32023|P|nw|38.0466|-116.4732
NV|041|LKN|Northeastern Nye County|NV041|Nye|32023|P|nw|38.5497|-115.8689
IN|076|LMK|Orange|IN076|Orange|18117|E|sc|38.5418|-86.4951
IN|077|LMK|Washington|IN077|Washington|18175|E|sc|38.6|-86.1053
IN|078|LMK|Scott|IN078|Scott|18143|E|sc|38.6851|-85.7474
IN|079|LMK|Jefferson|IN079|Jefferson|18077|E|sc|38.7858|-85.4385
IN|083|LMK|Dubois|IN083|Dubois|18037|C|sc|38.3643|-86.8798
IN|084|LMK|Crawford|IN084|Crawford|18025|E|sc|38.2923|-86.4517
IN|089|LMK|Perry|IN089|Perry|18123|C|sc|38.0797|-86.638
IN|090|LMK|Harrison|IN090|Harrison|18061|E|sc|38.1952|-86.1113
IN|091|LMK|Floyd|IN091|Floyd|18043|E|sc|38.3194|-85.9068
IN|092|LMK|Clark|IN092|Clark|18019|E|sc|38.4773|-85.7073
KY|023|LMK|Hancock|KY023|Hancock|21091|C|nw|37.8415|-86.778
KY|024|LMK|Breckinridge|KY024|Breckinridge|21027|C|nc|37.7732|-86.4293
KY|025|LMK|Meade|KY025|Meade|21163|E|nc|37.9695|-86.2169
KY|026|LMK|Ohio|KY026|Ohio|21183|C|nw|37.4783|-86.849
KY|027|LMK|Grayson|KY027|Grayson|21085|C|sc|37.4608|-86.3439
KY|028|LMK|Hardin|KY028|Hardin|21093|E|nc|37.6979|-85.9635
KY|029|LMK|Bullitt|KY029|Bullitt|21029|E|nc|37.97|-85.6959
KY|030|LMK|Jefferson|KY030|Jefferson|21111|E|nc|38.1872|-85.6595
KY|031|LMK|Oldham|KY031|Oldham|21185|E|nc|38.3995|-85.4485
KY|032|LMK|Trimble|KY032|Trimble|21223|E|nc|38.613|-85.3374
KY|033|LMK|Henry|KY033|Henry|21103|E|nc|38.4484|-85.1189
KY|034|LMK|Shelby|KY034|Shelby|21211|E|nc|38.2155|-85.1948
KY|035|LMK|Franklin|KY035|Franklin|21073|E|ec|38.2391|-84.877
KY|036|LMK|Scott|KY036|Scott|21209|E|ec|38.2915|-84.5839
KY|037|LMK|Harrison|KY037|Harrison|21097|E|ec|38.4418|-84.3315
KY|038|LMK|Spencer|KY038|Spencer|21215|E|nc|38.0325|-85.3279
KY|039|LMK|Anderson|KY039|Anderson|21005|E|ec|38.004|-84.9909
KY|040|LMK|Woodford|KY040|Woodford|21239|E|ec|38.0423|-84.7435
KY|041|LMK|Fayette|KY041|Fayette|21067|E|ec|38.0423|-84.4588
KY|042|LMK|Bourbon|KY042|Bourbon|21017|E|ec|38.2068|-84.2171
KY|043|LMK|Nicholas|KY043|Nicholas|21181|E|ec|38.3356|-84.0153
KY|045|LMK|Nelson|KY045|Nelson|21179|E|nc|37.8051|-85.4662
KY|046|LMK|Washington|KY046|Washington|21229|E|nc|37.7534|-85.1747
KY|047|LMK|Mercer|KY047|Mercer|21167|E|ec|37.8111|-84.8744
KY|048|LMK|Jessamine|KY048|Jessamine|21113|E|ec|37.872|-84.5809
KY|049|LMK|Clark|KY049|Clark|21049|E|ec|37.9709|-84.1475
KY|053|LMK|Larue|KY053|Larue|21123|E|nc|37.5457|-85.698
KY|054|LMK|Marion|KY054|Marion|21155|E|sc|37.5525|-85.2696
KY|055|LMK|Boyle|KY055|Boyle|21021|E|ec|37.6244|-84.8667
KY|056|LMK|Garrard|KY056|Garrard|21079|E|ec|37.6396|-84.5376
KY|057|LMK|Madison|KY057|Madison|21151|E|ec|37.7202|-84.278
KY|061|LMK|Butler|KY061|Butler|21031|C|sc|37.2074|-86.6816
KY|062|LMK|Edmonson|KY062|Edmonson|21061|C|sc|37.2087|-86.2385
KY|063|LMK|Hart|KY063|Hart|21099|C|sc|37.2999|-85.8847
KY|064|LMK|Green|KY064|Green|21087|C|sc|37.2639|-85.5531
KY|065|LMK|Taylor|KY065|Taylor|21217|E|sc|37.3664|-85.3279
KY|066|LMK|Casey|KY066|Casey|21045|E|sc|37.3223|-84.9283
KY|067|LMK|Lincoln|KY067|Lincoln|21137|E|sc|37.4552|-84.6607
KY|070|LMK|Logan|KY070|Logan|21141|C|sc|36.8597|-86.8788
KY|071|LMK|Warren|KY071|Warren|21227|C|sc|36.9936|-86.4239
KY|072|LMK|Simpson|KY072|Simpson|21213|C|sc|36.7419|-86.5823
KY|073|LMK|Allen|KY073|Allen|21003|C|sc|36.7513|-86.1904
KY|074|LMK|Barren|KY074|Barren|21009|C|sc|36.9656|-85.9336
KY|075|LMK|Monroe|KY075|Monroe|21171|C|sc|36.7122|-85.7164
KY|076|LMK|Metcalf|KY076|Metcalfe|21169|C|sc|36.9905|-85.6291
KY|077|LMK|Adair|KY077|Adair|21001|C|sc|37.1041|-85.2806
KY|078|LMK|Russell|KY078|Russell|21207|C|sc|36.9911|-85.0586
KY|081|LMK|Cumberland|KY081|Cumberland|21057|C|sc|36.7866|-85.3884
KY|082|LMK|Clinton|KY082|Clinton|21053|C|sc|36.7275|-85.1361
IL|003|LOT|Winnebago|IL003|Winnebago|17201|C|nc|42.3363|-89.1609
IL|004|LOT|Boone|IL004|Boone|17007|C|nc|42.3231|-88.8234
IL|005|LOT|McHenry|IL005|McHenry|17111|C|ne|42.3244|-88.4524
IL|006|LOT|Lake|IL006|Lake|17097|C|ne|42.3231|-88.0036
IL|008|LOT|Ogle|IL008|Ogle|17141|C|nc|42.0427|-89.3207
IL|010|LOT|Lee|IL010|Lee|17103|C|nc|41.7461|-89.3005
IL|011|LOT|De Kalb|IL011|De Kalb|17037|C|nc|41.8934|-88.7704
IL|012|LOT|Kane|IL012|Kane|17089|C|ne|41.939|-88.4287
IL|013|LOT|DuPage|IL013|DuPage|17043|C|ne|41.852|-88.0857
IL|019|LOT|La Salle|IL019|La Salle|17099|C|nc|41.3439|-88.8859
IL|020|LOT|Kendall|IL020|Kendall|17093|C|ne|41.5906|-88.4289
IL|021|LOT|Grundy|IL021|Grundy|17063|C|ne|41.2849|-88.4185
IL|023|LOT|Kankakee|IL023|Kankakee|17091|C|ne|41.1377|-87.8618
IL|032|LOT|Livingston|IL032|Livingston|17105|C|cc|40.8914|-88.5578
IL|033|LOT|Iroquois|IL033|Iroquois|17075|C|ec|40.7474|-87.8243
IL|039|LOT|Ford|IL039|Ford|17053|C|ec|40.5972|-88.2233
IL|103|LOT|Northern Cook|IL103|Cook|17031|C|ne|42.0711|-87.9824
IL|104|LOT|Central Cook|IL104|Cook|17031|C|ne|41.8208|-87.7444
IL|105|LOT|Southern Cook|IL105|Cook|17031|C|ne|41.5834|-87.7273
IL|106|LOT|Northern Will|IL106|Will|17197|C|ne|41.5776|-88.0699
IL|107|LOT|Southern Will|IL107|Will|17197|C|ne|41.3459|-88.0891
IL|108|LOT|Eastern Will|IL108|Will|17197|C|ne|41.3833|-87.7148
IN|001|LOT|Lake|IN001|Lake|18089|C|nw|41.4156|-87.3817
IN|002|LOT|Porter|IN002|Porter|18127|C|nw|41.4605|-87.0671
IN|010|LOT|Newton|IN010|Newton|18111|C|nw|40.9559|-87.3975
IN|011|LOT|Jasper|IN011|Jasper|18073|C|nw|41.023|-87.1162
IN|019|LOT|Benton|IN019|Benton|18007|E|nw|40.6063|-87.3109
CA|038|LOX|Cuyama Valley|CA038|Santa Barbara|06083|P|sw|34.9422|-119.7374
CA|087|LOX|Catalina Island|CA087|Los Angeles|06037|P|sw|33.382|-118.4331
CA|088|LOX|Santa Clarita Valley|CA088|Los Angeles|06037|P|sw|34.4534|-118.5579
CA|340|LOX|San Luis Obispo County Beaches|CA340|San Luis Obispo|06079|P|sw|35.3656|-120.8857
CA|341|LOX|San Luis Obispo County Inland Central Coast|CA341|San Luis Obispo|06079|P|sw|35.1214|-120.5471
CA|342|LOX|Santa Lucia Mountains|CA342|San Luis Obispo|06079|P|sw|35.4597|-120.795
CA|343|LOX|Southern Salinas Valley|CA343|San Luis Obispo|06079|P|sw|35.6395|-120.7122
CA|344|LOX|San Luis Obispo County Interior Valleys|CA344|San Luis Obispo|06079|P|sw|35.4405|-120.1532
CA|345|LOX|San Luis Obispo County Mountains|CA345|San Luis Obispo|06079|P|sw|35.1768|-120.1048
CA|346|LOX|Santa Barbara County Central Coast Beaches|CA346|Santa Barbara|06083|P|sw|34.7179|-120.5534
CA|347|LOX|Santa Barbara County Inland Central Coast|CA347|Santa Barbara|06083|P|sw|34.7553|-120.3762
CA|348|LOX|Santa Ynez Valley|CA348|Santa Barbara|06083|P|sw|34.6908|-120.0988
CA|349|LOX|Santa Barbara County Southwestern Coast|CA349|Santa Barbara|06083|P|sw|34.5052|-120.3013
CA|350|LOX|Santa Barbara County Southeastern Coast|CA350|Santa Barbara|06083|P|sw|34.4344|-119.7142
CA|351|LOX|Santa Ynez Mountains Western Range|CA351|Santa Barbara|06083|P|sw|34.5164|-119.9838
CA|352|LOX|Santa Ynez Mountains Eastern Range|CA352|Santa Barbara|06083|P|sw|34.4707|-119.548
CA|352|LOX|Santa Ynez Mountains Eastern Range|CA352|Ventura|06111|P|sw|34.4707|-119.548
CA|353|LOX|Santa Barbara County Interior Mountains|CA353|Santa Barbara|06083|P|sw|34.7747|-119.823
CA|354|LOX|Ventura County Beaches|CA354|Ventura|06111|P|sw|34.2116|-119.2077
CA|355|LOX|Ventura County Inland Coast|CA355|Ventura|06111|P|sw|34.2366|-119.0715
CA|356|LOX|Lake Casitas|CA356|Ventura|06111|P|sw|34.4011|-119.3447
CA|357|LOX|Ojai Valley|CA357|Ventura|06111|P|sw|34.4268|-119.2615
CA|358|LOX|Central Ventura County Valleys|CA358|Ventura|06111|P|sw|34.3897|-119.0367
CA|362|LOX|Malibu Coast|CA362|Los Angeles|06037|P|sw|34.0408|-118.6777
CA|366|LOX|Los Angeles County Beaches|CA366|Los Angeles|06037|P|sw|33.8457|-118.3308
CA|367|LOX|Palos Verdes Hills|CA367|Los Angeles|06037|P|sw|33.7652|-118.3624
CA|368|LOX|Los Angeles County Inland Coast including Downtown Los Angeles|CA368|Los Angeles|06037|P|sw|33.9486|-118.2407
CA|369|LOX|Western Santa Monica Mountains|CA369|Los Angeles|06037|P|sw|34.0907|-118.889
CA|369|LOX|Western Santa Monica Mountains|CA369|Ventura|06111|P|sw|34.0907|-118.889
CA|370|LOX|Eastern Santa Monica Mountains|CA370|Los Angeles|06037|P|sw|34.0938|-118.5622
CA|371|LOX|Calabasas and Agoura Hills|CA371|Los Angeles|06037|P|sw|34.1299|-118.7423
CA|372|LOX|Western San Fernando Valley|CA372|Los Angeles|06037|P|sw|34.2249|-118.5083
CA|373|LOX|Eastern San Fernando Valley|CA373|Los Angeles|06037|P|sw|34.1898|-118.2987
CA|374|LOX|Southeastern Ventura County Valleys|CA374|Ventura|06111|P|sw|34.2322|-118.8394
CA|375|LOX|Santa Susana Mountains|CA375|Los Angeles|06037|P|sw|34.3387|-118.7386
CA|375|LOX|Santa Susana Mountains|CA375|Ventura|06111|P|sw|34.543|-119.0936
CA|376|LOX|Southern Ventura County Mountains|CA376|Ventura|06111|P|sw|34.543|-119.0936
CA|377|LOX|Northern Ventura County Mountains|CA377|Ventura|06111|P|sw|34.7342|-119.1611
CA|378|LOX|Northwestern Los Angeles County Mountains including the Interstate 5 Corridor|CA378|Los Angeles|06037|P|sw|34.6716|-118.7273
CA|379|LOX|Western San Gabriel Mountains including the Highway 14 Corridor|CA379|Los Angeles|06037|P|sw|34.4617|-118.2964
CA|380|LOX|Eastern San Gabriel Mountains|CA380|Los Angeles|06037|P|sw|34.2905|-117.8806
CA|381|LOX|Western Antelope Valley Foothills|CA381|Los Angeles|06037|P|sw|34.6494|-118.3779
CA|382|LOX|Eastern Antelope Valley Foothills|CA382|Los Angeles|06037|P|sw|34.4909|-117.8141
CA|383|LOX|Antelope Valley |CA383|Los Angeles|06037|P|sw|34.7001|-118.0482
CA|548|LOX|Los Angeles County San Gabriel Valley|CA548|Los Angeles|06037|P|sw|34.0657|-117.9738
CA|549|LOX|San Miguel and Santa Rosa Islands|CA549|Santa Barbara|06083|P|sw|33.9774|-120.1462
CA|550|LOX|Santa Cruz and Anacapa Islands|CA550|Santa Barbara|06083|P|sw|34.0138|-119.7416
IL|058|LSX|Greene|IL058|Greene|17061|C|sw|39.3562|-90.3905
IL|059|LSX|Macoupin|IL059|Macoupin|17117|C|sw|39.261|-89.9244
IL|060|LSX|Montgomery|IL060|Montgomery|17135|C|sc|39.231|-89.4789
IL|064|LSX|Bond|IL064|Bond|17005|C|sc|38.8868|-89.4356
IL|065|LSX|Fayette|IL065|Fayette|17051|C|sc|39.0002|-89.0242
IL|069|LSX|Clinton|IL069|Clinton|17027|C|sc|38.6065|-89.4224
IL|070|LSX|Marion|IL070|Marion|17121|C|sc|38.6496|-88.919
IL|074|LSX|Washington|IL074|Washington|17189|C|sc|38.3522|-89.4105
IL|079|LSX|Randolph|IL079|Randolph|17157|C|sw|38.0521|-89.8253
IL|095|LSX|Adams|IL095|Adams|17001|C|wc|39.9878|-91.1886
IL|096|LSX|Brown|IL096|Brown|17009|C|wc|39.9618|-90.7504
IL|097|LSX|Pike|IL097|Pike|17149|C|wc|39.6225|-90.8863
IL|098|LSX|Calhoun|IL098|Calhoun|17013|C|sw|39.1692|-90.6675
IL|099|LSX|Jersey|IL099|Jersey|17083|C|sw|39.0856|-90.3566
IL|100|LSX|Madison|IL100|Madison|17119|C|sw|38.8299|-89.9051
IL|101|LSX|St. Clair|IL101|St. Clair|17163|C|sw|38.4703|-89.9284
IL|102|LSX|Monroe|IL102|Monroe|17133|C|sw|38.2785|-90.1774
MO|018|LSX|Knox|MO018|Knox|29103|C|ne|40.1282|-92.1481
MO|019|LSX|Lewis|MO019|Lewis|29111|C|ne|40.0969|-91.7222
MO|026|LSX|Shelby|MO026|Shelby|29205|C|ne|39.7978|-92.0766
MO|027|LSX|Marion|MO027|Marion|29127|C|ne|39.806|-91.6224
MO|034|LSX|Monroe|MO034|Monroe|29137|C|ne|39.4955|-92.0007
MO|035|LSX|Ralls|MO035|Ralls|29173|C|ne|39.5276|-91.522
MO|036|LSX|Pike|MO036|Pike|29163|C|ne|39.3438|-91.1714
MO|041|LSX|Boone|MO041|Boone|29019|C|cc|38.9907|-92.3096
MO|042|LSX|Audrain|MO042|Audrain|29007|C|cc|39.2158|-91.8416
MO|047|LSX|Moniteau|MO047|Moniteau|29135|C|cc|38.6327|-92.5831
MO|048|LSX|Cole|MO048|Cole|29051|C|cc|38.5055|-92.2816
MO|049|LSX|Osage|MO049|Osage|29151|C|cc|38.4604|-91.8618
MO|050|LSX|Callaway|MO050|Callaway|29027|C|cc|38.8355|-91.926
MO|051|LSX|Montgomery|MO051|Montgomery|29139|C|ec|38.9415|-91.4702
MO|052|LSX|Lincoln|MO052|Lincoln|29113|C|ec|39.0581|-90.9602
MO|059|LSX|Gasconade|MO059|Gasconade|29073|C|ec|38.4409|-91.5079
MO|060|LSX|Warren|MO060|Warren|29219|C|ec|38.7646|-91.1607
MO|061|LSX|St. Charles|MO061|St. Charles|29183|C|ec|38.7819|-90.6752
MO|062|LSX|Franklin|MO062|Franklin|29071|C|ec|38.4112|-91.075
MO|063|LSX|St. Louis|MO063|St. Louis|29189|C|ec|38.6407|-90.443
MO|064|LSX|St. Louis City|MO064|St. Louis City|29510|C|ec|38.6358|-90.245
MO|065|LSX|Jefferson|MO065|Jefferson|29099|C|ec|38.261|-90.5378
MO|072|LSX|Crawford|MO072|Crawford|29055|C|ec|37.9764|-91.304
MO|073|LSX|Washington|MO073|Washington|29221|C|ec|37.9617|-90.8774
MO|074|LSX|St. Francois|MO074|St. Francois|29187|C|se|37.8104|-90.4729
MO|075|LSX|Ste. Genevieve|MO075|Ste. Genevieve|29186|C|se|37.894|-90.1952
MO|084|LSX|Iron|MO084|Iron|29093|C|se|37.5552|-90.7735
MO|085|LSX|Madison|MO085|Madison|29123|C|se|37.4781|-90.345
MO|099|LSX|Reynolds|MO099|Reynolds|29179|C|se|37.3623|-90.9691
TX|021|LUB|Parmer|TX021|Parmer|48369|C|pa|34.5301|-102.7845
TX|022|LUB|Castro|TX022|Castro|48069|C|pa|34.53|-102.2617
TX|023|LUB|Swisher|TX023|Swisher|48437|C|pa|34.5304|-101.735
TX|024|LUB|Briscoe|TX024|Briscoe|48045|C|pa|34.5303|-101.2086
TX|025|LUB|Hall|TX025|Hall|48191|C|pa|34.5308|-100.6811
TX|026|LUB|Childress|TX026|Childress|48075|C|pa|34.5292|-100.2076
TX|027|LUB|Bailey|TX027|Bailey|48017|C|nw|34.0685|-102.8298
TX|028|LUB|Lamb|TX028|Lamb|48279|C|nw|34.0686|-102.3517
TX|029|LUB|Hale|TX029|Hale|48189|C|nw|34.0705|-101.8269
TX|030|LUB|Floyd|TX030|Floyd|48153|C|nw|34.0724|-101.3032
TX|031|LUB|Motley|TX031|Motley|48345|C|nw|34.0741|-100.7798
TX|032|LUB|Cottle|TX032|Cottle|48101|C|nw|34.0776|-100.2788
TX|033|LUB|Cochran|TX033|Cochran|48079|C|nw|33.6041|-102.8285
TX|034|LUB|Hockley|TX034|Hockley|48219|C|nw|33.6076|-102.3432
TX|035|LUB|Lubbock|TX035|Lubbock|48303|C|nw|33.6102|-101.8205
TX|036|LUB|Crosby|TX036|Crosby|48107|C|nw|33.6146|-101.3
TX|037|LUB|Dickens|TX037|Dickens|48125|C|nw|33.6166|-100.7789
TX|038|LUB|King|TX038|King|48269|C|nw|33.6165|-100.2558
TX|039|LUB|Yoakum|TX039|Yoakum|48501|C|nw|33.173|-102.8278
TX|040|LUB|Terry|TX040|Terry|48445|C|nw|33.1738|-102.3352
TX|041|LUB|Lynn|TX041|Lynn|48305|C|nw|33.1768|-101.8161
TX|042|LUB|Garza|TX042|Garza|48169|C|nw|33.1799|-101.2984
TX|043|LUB|Kent|TX043|Kent|48263|C|nw|33.1814|-100.7776
TX|044|LUB|Stonewall|TX044|Stonewall|48433|C|nw|33.1791|-100.2533
DC|001|LWX|District of Columbia|DC001|District of Columbia|11001|E||38.9093|-77.0146
MD|001|LWX|Garrett|MD001|Garrett|24023|E|ww|39.5286|-79.2739
MD|003|LWX|Washington|MD003|Washington|24043|E|nc|39.6037|-77.8142
MD|004|LWX|Frederick|MD004|Frederick|24021|E|nc|39.4722|-77.3981
MD|005|LWX|Carroll|MD005|Carroll|24013|E|nc|39.5631|-77.0227
MD|006|LWX|Northern Baltimore|MD006|Baltimore|24005|E|nn|39.5444|-76.6677
MD|008|LWX|Cecil|MD008|Cecil|24015|E|ne|39.4885|-75.9418
MD|008|LWX|Cecil|MD008|Cecil|24015|E|ne|39.5749|-75.9384
MD|011|LWX|Southern Baltimore|MD011|Baltimore|24005|E|nn|39.2929|-76.4049
MD|011|LWX|Southern Baltimore|MD011|Baltimore|24005|E|nn|39.3312|-76.6096
MD|011|LWX|Southern Baltimore|MD011|Baltimore City|24510|E|nn|39.3312|-76.6096
MD|013|LWX|Prince Georges|MD013|Prince Georges|24033|E|cc|38.8313|-76.8436
MD|014|LWX|Anne Arundel|MD014|Anne Arundel|24003|E|cc|38.933|-76.528
MD|014|LWX|Anne Arundel|MD014|Anne Arundel|24003|E|cc|39.0074|-76.6088
MD|016|LWX|Charles|MD016|Charles|24017|E|ss|38.3923|-76.9809
MD|016|LWX|Charles|MD016|Charles|24017|E|ss|38.5078|-76.99
MD|017|LWX|St. Marys|MD017|St. Marys|24037|E|ss|38.2233|-76.6289
MD|017|LWX|St. Marys|MD017|St. Marys|24037|E|ss|38.3046|-76.6081
MD|018|LWX|Calvert|MD018|Calvert|24009|E|ss|38.5513|-76.5696
MD|501|LWX|Extreme Western Allegany|MD501|Allegany|24001|E|ww|39.6015|-78.9284
MD|502|LWX|Central and Eastern Allegany|MD502|Allegany|24001|E|ww|39.6304|-78.597
MD|503|LWX|Northwest Montgomery|MD503|Montgomery|24031|E|cc|39.1949|-77.3233
MD|504|LWX|Central and Southeast Montgomery|MD504|Montgomery|24031|E|cc|39.0917|-77.1134
MD|505|LWX|Northwest Howard|MD505|Howard|24027|E|cc|39.3234|-77.0597
MD|506|LWX|Central and Southeast Howard|MD506|Howard|24027|E|cc|39.2259|-76.8872
MD|507|LWX|Northwest Harford|MD507|Harford|24025|E|nn|39.6258|-76.3985
MD|508|LWX|Southeast Harford|MD508|Harford|24025|E|nn|39.6395|-76.3985
VA|526|LWX|Northwest Prince William|VA526|Prince William|51153|E|nn|38.8549|-77.6332
VA|527|LWX|Central and Southeast Prince William/Manassas/Manassas Park|VA527|Prince William|51153|E|nn|38.6727|-77.4488
VA|527|LWX|Central and Southeast Prince William/Manassas/Manassas Park|VA527|City of Manassas|51683|E|nn|38.6727|-77.4488
VA|527|LWX|Central and Southeast Prince William/Manassas/Manassas Park|VA527|City of Manassas Park|51685|E|nn|38.6727|-77.4488
VA|025|LWX|Augusta|VA025|City of Staunton|51790|E|ww|38.163|-79.1289
VA|025|LWX|Augusta|VA025|City of Waynesboro|51820|E|ww|38.163|-79.1289
VA|026|LWX|Rockingham|VA026|Rockingham|51165|E|ww|38.5106|-78.8757
VA|026|LWX|Rockingham|VA026|City of Harrisonburg|51660|E|ww|38.5106|-78.8757
VA|027|LWX|Shenandoah|VA027|Shenandoah|51171|E|nw|38.8585|-78.5704
VA|028|LWX|Frederick|VA028|Frederick|51069|E|nw|39.2039|-78.2606
VA|028|LWX|Frederick|VA028|City of Winchester|51840|E|nw|39.2039|-78.2606
VA|029|LWX|Page|VA029|Page|51139|E|nw|38.62|-78.4841
VA|030|LWX|Warren|VA030|Warren|51187|E|nw|38.9087|-78.2072
VA|031|LWX|Clarke|VA031|Clarke|51043|E|nw|39.1122|-77.9966
VA|036|LWX|Nelson|VA036|Nelson|51125|E|cc|37.7874|-78.8867
VA|037|LWX|Albemarle|VA037|City of Charlottesville|51540|E|cc|38.0231|-78.5555
VA|038|LWX|Greene|VA038|Greene|51079|E|cc|38.2977|-78.4669
VA|039|LWX|Madison|VA039|Madison|51113|E|nw|38.4137|-78.2792
VA|040|LWX|Rappahannock|VA040|Rappahannock|51157|E|nw|38.6845|-78.1593
VA|050|LWX|Orange|VA050|Orange|51137|E|cc|38.2463|-78.0134
VA|051|LWX|Culpeper|VA051|Culpeper|51047|E|nn|38.4861|-77.9559
VA|053|LWX|Fairfax|VA053|Fairfax|51059|E|nn|38.8387|-77.2791
VA|053|LWX|Fairfax|VA053|City of Fairfax|51600|E|nn|38.8387|-77.2791
VA|054|LWX|Arlington/Falls Church/Alexandria|VA054|Arlington|51013|E|nn|38.8577|-77.0989
VA|054|LWX|Arlington/Falls Church/Alexandria|VA054|City of Alexandria|51510|E|nn|38.8577|-77.0989
VA|054|LWX|Arlington/Falls Church/Alexandria|VA054|City of Falls Church|51610|E|nn|38.8577|-77.0989
VA|055|LWX|Stafford|VA055|Stafford|51179|E|nn|38.4213|-77.4603
VA|056|LWX|Spotsylvania|VA056|Spotsylvania|51177|E|cc|38.1882|-77.6525
VA|056|LWX|Spotsylvania|VA056|City of Fredericksburg|51630|E|cc|38.1882|-77.6525
VA|057|LWX|King George|VA057|King George|51099|E|cc|38.2729|-77.1572
VA|501|LWX|Northern Fauquier|VA501|Fauquier|51061|E|nn|38.854|-77.8851
VA|502|LWX|Southern Fauquier|VA502|Fauquier|51061|E|nn|38.5953|-77.7154
VA|503|LWX|Western Highland|VA503|Highland|51091|E|ww|38.4256|-79.6618
VA|504|LWX|Eastern Highland|VA504|Highland|51091|E|ww|38.3315|-79.523
VA|505|LWX|Western Loudoun|VA505|Loudoun|51107|E|nn|39.1337|-77.6963
VA|506|LWX|Eastern Loudoun|VA506|Loudoun|51107|E|nn|39.0052|-77.5151
VA|507|LWX|Northern Virginia Blue Ridge|VA507|Greene|51079|E|cc|38.5272|-78.4323
VA|507|LWX|Northern Virginia Blue Ridge|VA507|Madison|51113|E|nw|38.5272|-78.4323
VA|507|LWX|Northern Virginia Blue Ridge|VA507|Page|51139|E|nw|38.5272|-78.4323
VA|507|LWX|Northern Virginia Blue Ridge|VA507|Rappahannock|51157|E|nw|38.5272|-78.4323
VA|507|LWX|Northern Virginia Blue Ridge|VA507|Rockingham|51165|E|ww|38.5272|-78.4323
VA|507|LWX|Northern Virginia Blue Ridge|VA507|Warren|51187|E|nw|38.5272|-78.4323
VA|508|LWX|Central Virginia Blue Ridge|VA508|Albemarle|51003|E|cc|37.9889|-78.9469
VA|508|LWX|Central Virginia Blue Ridge|VA508|Augusta|51015|E|ww|37.9889|-78.9469
WV|050|LWX|Hampshire|WV050|Hampshire|54027|E|ee|39.3171|-78.6142
WV|051|LWX|Morgan|WV051|Morgan|54065|E|pa|39.5604|-78.2578
WV|052|LWX|Berkeley|WV052|Berkeley|54003|E|pa|39.4641|-78.0275
WV|053|LWX|Jefferson|WV053|Jefferson|54037|E|pa|39.3076|-77.8628
WV|055|LWX|Hardy|WV055|Hardy|54031|E|ee|39.0075|-78.8579
WV|501|LWX|Western Grant|WV501|Grant|54023|E|ee|39.2245|-79.2815
WV|502|LWX|Eastern Grant|WV502|Grant|54023|E|ee|39.0552|-79.1596
WV|503|LWX|Western Mineral|WV503|Mineral|54057|E|ee|39.3868|-79.1158
WV|504|LWX|Eastern Mineral|WV504|Mineral|54057|E|ee|39.4239|-78.8872
WV|505|LWX|Western Pendleton|WV505|Pendleton|54071|E|ee|38.7534|-79.4656
WV|506|LWX|Eastern Pendleton|WV506|Pendleton|54071|E|ee|38.6434|-79.2919
AR|004|LZK|Marion|AR004|Marion|05089|C|nc|36.2684|-92.6842
AR|005|LZK|Baxter|AR005|Baxter|05005|C|nc|36.2872|-92.337
AR|006|LZK|Fulton|AR006|Fulton|05049|C|nc|36.3817|-91.8183
AR|007|LZK|Sharp|AR007|Sharp|05135|C|nc|36.1611|-91.4799
AR|008|LZK|Randolph|AR008|Randolph|05121|C|ee|36.3415|-91.0278
AR|014|LZK|Stone|AR014|Stone|05137|C|nc|35.8599|-92.1567
AR|015|LZK|Izard|AR015|Izard|05065|C|nc|36.0949|-91.9134
AR|016|LZK|Independence|AR016|Independence|05063|C|nc|35.7415|-91.5698
AR|017|LZK|Lawrence|AR017|Lawrence|05075|C|ee|36.0413|-91.1071
AR|024|LZK|Cleburne|AR024|Cleburne|05023|C|nc|35.5381|-92.0267
AR|025|LZK|Jackson|AR025|Jackson|05067|C|ee|35.5994|-91.2146
AR|031|LZK|Conway|AR031|Conway|05029|C|cc|35.2622|-92.7014
AR|032|LZK|Faulkner|AR032|Faulkner|05045|C|cc|35.147|-92.3321
AR|033|LZK|White|AR033|White|05145|C|cc|35.2563|-91.7457
AR|034|LZK|Woodruff|AR034|Woodruff|05147|C|ee|35.1863|-91.2431
AR|039|LZK|Perry|AR039|Perry|05105|C|cc|34.9474|-92.9315
AR|042|LZK|Garland|AR042|Garland|05051|C|cc|34.5767|-93.1504
AR|043|LZK|Saline|AR043|Saline|05125|C|cc|34.6466|-92.6766
AR|044|LZK|Pulaski|AR044|Pulaski|05119|C|cc|34.7699|-92.3118
AR|045|LZK|Lonoke|AR045|Lonoke|05085|C|cc|34.7542|-91.8887
AR|046|LZK|Prairie|AR046|Prairie|05117|C|cc|34.8297|-91.5528
AR|047|LZK|Monroe|AR047|Monroe|05095|C|ee|34.6778|-91.2038
AR|052|LZK|Pike|AR052|Pike|05109|C|sw|34.1636|-93.6564
AR|053|LZK|Clark|AR053|Clark|05019|C|sw|34.051|-93.1764
AR|054|LZK|Hot Spring|AR054|Hot Spring|05059|C|sw|34.3177|-92.946
AR|055|LZK|Grant|AR055|Grant|05053|C|cc|34.29|-92.4236
AR|056|LZK|Jefferson|AR056|Jefferson|05069|C|se|34.2688|-91.9315
AR|057|LZK|Arkansas|AR057|Arkansas|05001|C|se|34.2908|-91.3749
AR|062|LZK|Dallas|AR062|Dallas|05039|C|sw|33.9698|-92.6545
AR|063|LZK|Cleveland|AR063|Cleveland|05025|C|se|33.8984|-92.1852
AR|064|LZK|Lincoln|AR064|Lincoln|05079|C|se|33.9575|-91.7333
AR|065|LZK|Desha|AR065|Desha|05041|C|se|33.8333|-91.254
AR|066|LZK|Ouachita|AR066|Ouachita|05103|C|sw|33.5933|-92.882
AR|067|LZK|Calhoun|AR067|Calhoun|05013|C|sw|33.558|-92.5031
AR|068|LZK|Bradley|AR068|Bradley|05011|C|se|33.4659|-92.1622
AR|069|LZK|Drew|AR069|Drew|05043|C|se|33.5895|-91.72
AR|103|LZK|Boone County Except Southwest|AR103|Boone|05009|C|nc|36.3217|-93.0755
AR|112|LZK|Newton County Higher Elevations|AR112|Newton|05101|C|nc|35.8956|-93.2439
AR|113|LZK|Searcy County Lower Elevations|AR113|Searcy|05129|C|nc|35.9775|-92.7213
AR|121|LZK|Southern Johnson County|AR121|Johnson|05071|C|ww|35.4736|-93.4744
AR|122|LZK|Southern Pope County|AR122|Pope|05115|C|cc|35.3423|-93.0596
AR|123|LZK|Southeast Van Buren County|AR123|Van Buren|05141|C|nc|35.5067|-92.4247
AR|130|LZK|Western and Northern Logan County|AR130|Logan|05083|C|ww|35.2523|-93.7455
AR|137|LZK|Northern Scott County|AR137|Scott|05127|C|ww|34.9845|-94.0579
AR|138|LZK|Northwest Yell County|AR138|Yell|05149|C|cc|35.1143|-93.5043
AR|140|LZK|Polk County Lower Elevations|AR140|Polk|05113|C|ww|34.4133|-94.3073
AR|141|LZK|Central and Eastern Montgomery County|AR141|Montgomery|05097|C|ww|34.5241|-93.6079
AR|203|LZK|Boone County Higher Elevations|AR203|Boone|05009|C|nc|36.1834|-93.2439
AR|212|LZK|Newton County Lower Elevations|AR212|Newton|05101|C|nc|36.0553|-93.0733
AR|213|LZK|Northwest Searcy County Higher Elevations|AR213|Searcy|05129|C|nc|36.0493|-92.8685
AR|221|LZK|Johnson County Higher Elevations|AR221|Johnson|05071|C|ww|35.6552|-93.4471
AR|222|LZK|Pope County Higher Elevations|AR222|Pope|05115|C|cc|35.607|-92.9956
AR|223|LZK|Van Buren County Higher Elevations|AR223|Van Buren|05141|C|nc|35.6487|-92.5994
AR|230|LZK|Southern and Eastern Logan County|AR230|Logan|05083|C|ww|35.1586|-93.6717
AR|237|LZK|Central and Southern Scott County|AR237|Scott|05127|C|ww|34.8189|-94.0651
AR|238|LZK|Yell Excluding Northwest|AR238|Yell|05149|C|cc|34.9695|-93.3837
AR|240|LZK|Northern Polk County Higher Elevations|AR240|Polk|05113|C|ww|34.6452|-94.2329
AR|241|LZK|Northern Montgomery County Higher Elevations|AR241|Montgomery|05097|C|ww|34.6914|-93.6775
AR|313|LZK|Eastern, Central, and Southern Searcy County Higher Elevations|AR313|Searcy|05129|C|nc|35.8697|-92.6677
AR|340|LZK|Southeast Polk County Higher Elevations|AR340|Polk|05113|C|ww|34.4489|-94.1274
AR|341|LZK|Southwest Montgomery County Higher Elevations|AR341|Montgomery|05097|C|ww|34.4197|-93.8217
NM|027|MAF|Guadalupe Mountains of Eddy County|NM027|Eddy|35015|M|se|32.239|-104.7304
NM|028|MAF|Eddy County Plains|NM028|Eddy|35015|M|se|32.4993|-104.2534
NM|029|MAF|Northern Lea County|NM029|Lea|35025|M|se|33.282|-103.4057
NM|033|MAF|Central Lea County|NM033|Lea|35025|M|se|32.7504|-103.4363
NM|034|MAF|Southern Lea County|NM034|Lea|35025|M|se|32.2502|-103.3937
TX|045|MAF|Gaines|TX045|Gaines|48165|C|ww|32.7407|-102.6352
TX|046|MAF|Dawson|TX046|Dawson|48115|C|ww|32.7425|-101.9477
TX|047|MAF|Borden|TX047|Borden|48033|C|ww|32.7437|-101.4317
TX|048|MAF|Scurry|TX048|Scurry|48415|C|ww|32.7463|-100.9164
TX|050|MAF|Andrews|TX050|Andrews|48003|C|ww|32.305|-102.6378
TX|051|MAF|Martin|TX051|Martin|48317|C|ww|32.3061|-101.9512
TX|052|MAF|Howard|TX052|Howard|48227|C|ww|32.3062|-101.4355
TX|053|MAF|Mitchell|TX053|Mitchell|48335|C|ww|32.3062|-100.9212
TX|059|MAF|Loving|TX059|Loving|48301|C|ww|31.8492|-103.58
TX|060|MAF|Winkler|TX060|Winkler|48495|C|ww|31.85|-103.0482
TX|061|MAF|Ector|TX061|Ector|48135|C|ww|31.8692|-102.5428
TX|062|MAF|Midland|TX062|Midland|48329|C|ww|31.8692|-102.0316
TX|063|MAF|Glasscock|TX063|Glasscock|48173|C|ww|31.8695|-101.5208
TX|067|MAF|Ward|TX067|Ward|48475|C|ww|31.5095|-103.1024
TX|068|MAF|Crane|TX068|Crane|48103|C|ww|31.4285|-102.5155
TX|069|MAF|Upton|TX069|Upton|48461|C|ww|31.3688|-102.043
TX|070|MAF|Reagan|TX070|Reagan|48383|C|ww|31.3662|-101.523
TX|075|MAF|Pecos|TX075|Pecos|48371|C|sw|30.7811|-102.7236
TX|082|MAF|Terrell|TX082|Terrell|48443|C|sw|30.225|-102.0765
TX|270|MAF|Guadalupe Mountains Above 7000 Feet |TX270|Culberson|48109|CM|sw|31.9461|-104.8425
TX|271|MAF|Guadalupe and Delaware Mountains |TX271|Culberson|48109|CM|sw|31.7378|-104.7322
TX|272|MAF|Van Horn and Highway 54 Corridor |TX272|Culberson|48109|CM|sw|31.2123|-104.7304
TX|273|MAF|Eastern Culberson County |TX273|Culberson|48109|CM|sw|31.6552|-104.3586
TX|274|MAF|Reeves County Plains |TX274|Reeves|48389|C|sw|31.3331|-103.68
TX|275|MAF|Chinati Mountains |TX275|Presidio|48377|C|sw|30.0939|-104.3962
TX|276|MAF|Marfa Plateau |TX276|Jeff Davis|48243|C|sw|30.179|-104.2468
TX|276|MAF|Marfa Plateau |TX276|Presidio|48377|C|sw|30.179|-104.2468
TX|277|MAF|Davis Mountains |TX277|Brewster|48043|C|sw|30.5275|-103.985
TX|277|MAF|Davis Mountains |TX277|Jeff Davis|48243|C|sw|30.5275|-103.985
TX|277|MAF|Davis Mountains |TX277|Presidio|48377|C|sw|30.5275|-103.985
TX|278|MAF|Davis Mountains Foothills |TX278|Brewster|48043|C|sw|30.7538|-103.787
TX|278|MAF|Davis Mountains Foothills |TX278|Culberson|48109|CM|sw|30.7538|-103.787
TX|278|MAF|Davis Mountains Foothills |TX278|Jeff Davis|48243|C|sw|30.7538|-103.787
TX|278|MAF|Davis Mountains Foothills |TX278|Reeves|48389|C|sw|30.7538|-103.787
TX|279|MAF|Central Brewster County |TX279|Brewster|48043|C|sw|29.8383|-103.3132
TX|280|MAF|Chisos Basin |TX280|Brewster|48043|C|sw|29.2508|-103.2892
TX|281|MAF|Presidio Valley |TX281|Culberson|48109|CM|sw|29.8815|-104.3805
TX|281|MAF|Presidio Valley |TX281|Jeff Davis|48243|C|sw|29.8815|-104.3805
TX|281|MAF|Presidio Valley |TX281|Presidio|48377|C|sw|29.8815|-104.3805
TX|282|MAF|Lower Brewster County |TX282|Brewster|48043|C|sw|29.5252|-103.0214
AR|009|MEG|Clay|AR009|Clay|05021|C|ee|36.3685|-90.4173
AR|018|MEG|Greene|AR018|Greene|05055|C|ee|36.1177|-90.5591
AR|026|MEG|Craighead|AR026|Craighead|05031|C|ee|35.8308|-90.6328
AR|027|MEG|Poinsett|AR027|Poinsett|05111|C|ee|35.574|-90.6629
AR|028|MEG|Mississippi|AR028|Mississippi|05093|C|ee|35.7639|-90.054
AR|035|MEG|Cross|AR035|Cross|05037|C|ee|35.2958|-90.7713
AR|036|MEG|Crittenden|AR036|Crittenden|05035|C|ee|35.2079|-90.3089
AR|048|MEG|St. Francis|AR048|St. Francis|05123|C|ee|35.022|-90.7478
AR|049|MEG|Lee|AR049|Lee|05077|C|ee|34.7806|-90.782
AR|058|MEG|Phillips|AR058|Phillips|05107|C|ee|34.4283|-90.848
MO|113|MEG|Dunklin|MO113|Dunklin|29069|C|se|36.2719|-90.0909
MO|115|MEG|Pemiscot|MO115|Pemiscot|29155|C|se|36.2111|-89.7858
MS|001|MEG|DeSoto|MS001|DeSoto|28033|C|ne|34.8754|-89.9918
MS|002|MEG|Marshall|MS002|Marshall|28093|C|nw|34.7623|-89.5031
MS|003|MEG|Benton|MS003|Benton|28009|C|ne|34.8173|-89.1885
MS|004|MEG|Tippah|MS004|Tippah|28139|C|ne|34.7684|-88.9089
MS|005|MEG|Alcorn|MS005|Alcorn|28003|C|ne|34.8808|-88.5803
MS|006|MEG|Tishomingo|MS006|Tishomingo|28141|C|ne|34.7404|-88.2393
MS|007|MEG|Tunica|MS007|Tunica|28143|C|nw|34.652|-90.3755
MS|008|MEG|Tate|MS008|Tate|28137|C|nw|34.6503|-89.9448
MS|009|MEG|Prentiss|MS009|Prentiss|28117|C|ne|34.6183|-88.5201
MS|010|MEG|Coahoma|MS010|Coahoma|28027|C|nw|34.2292|-90.6027
MS|011|MEG|Quitman|MS011|Quitman|28119|C|nw|34.2514|-90.2891
MS|012|MEG|Panola|MS012|Panola|28107|C|nw|34.3639|-89.9505
MS|013|MEG|Lafayette|MS013|Lafayette|28071|C|nw|34.3568|-89.4849
MS|014|MEG|Union|MS014|Union|28145|C|ne|34.4905|-89.0038
MS|015|MEG|Pontotoc|MS015|Pontotoc|28115|C|ne|34.2254|-89.0374
MS|016|MEG|Lee|MS016|Lee|28081|C|ne|34.2899|-88.6804
MS|017|MEG|Itawamba|MS017|Itawamba|28057|C|ne|34.28|-88.3613
MS|020|MEG|Tallahatchie|MS020|Tallahatchie|28135|C|nw|33.9505|-90.1732
MS|021|MEG|Yalobusha|MS021|Yalobusha|28161|C|nw|34.0282|-89.7076
MS|022|MEG|Calhoun|MS022|Calhoun|28013|C|ne|33.9364|-89.3364
MS|023|MEG|Chickasaw|MS023|Chickasaw|28017|C|ne|33.9208|-88.9479
MS|024|MEG|Monroe|MS024|Monroe|28095|C|ne|33.8923|-88.4804
TN|001|MEG|Lake|TN001|Lake|47095|C|nw|36.3352|-89.4935
TN|002|MEG|Obion|TN002|Obion|47131|C|nw|36.3582|-89.1488
TN|003|MEG|Weakley|TN003|Weakley|47183|C|nw|36.2983|-88.7178
TN|004|MEG|Henry|TN004|Henry|47079|C|nw|36.3317|-88.3013
TN|019|MEG|Dyer|TN019|Dyer|47045|C|nw|36.059|-89.4138
TN|020|MEG|Gibson|TN020|Gibson|47053|C|nw|35.9966|-88.9326
TN|021|MEG|Carroll|TN021|Carroll|47017|C|nw|35.9731|-88.4502
TN|048|MEG|Lauderdale|TN048|Lauderdale|47097|C|sw|35.7609|-89.6314
TN|049|MEG|Tipton|TN049|Tipton|47167|C|sw|35.4966|-89.7594
TN|050|MEG|Haywood|TN050|Haywood|47075|C|sw|35.5833|-89.2838
TN|051|MEG|Crockett|TN051|Crockett|47033|C|nw|35.8135|-89.1395
TN|052|MEG|Madison|TN052|Madison|47113|C|sw|35.6082|-88.8385
TN|053|MEG|Chester|TN053|Chester|47023|C|sw|35.4211|-88.6128
TN|054|MEG|Henderson|TN054|Henderson|47077|C|sw|35.6543|-88.388
TN|055|MEG|Decatur|TN055|Decatur|47039|C|mi|35.603|-88.1088
TN|088|MEG|Shelby|TN088|Shelby|47157|C|sw|35.1837|-89.8956
TN|089|MEG|Fayette|TN089|Fayette|47047|C|sw|35.1971|-89.4144
TN|090|MEG|Hardeman|TN090|Hardeman|47069|C|sw|35.2069|-88.9931
TN|091|MEG|McNairy|TN091|McNairy|47109|C|sw|35.1746|-88.5637
TN|092|MEG|Hardin|TN092|Hardin|47071|C|sw|35.1987|-88.1845
FL|063|MFL|Glades|FL063|Glades|12043|E|ss|26.9605|-81.2397
FL|066|MFL|Hendry|FL066|Hendry|12051|E|ss|26.5473|-81.1718
FL|067|MFL|Inland Palm Beach County|FL067|Palm Beach|12099|E|se|26.6172|-80.5109
FL|068|MFL|Metro Palm Beach County|FL068|Palm Beach|12099|E|se|26.6222|-80.1464
FL|069|MFL|Coastal Collier County|FL069|Collier|12021|E|sw|26.015|-81.6017
FL|070|MFL|Inland Collier County|FL070|Collier|12021|E|sw|26.138|-81.293
FL|071|MFL|Inland Broward County|FL071|Broward|12011|E|se|26.1632|-80.6145
FL|072|MFL|Metro Broward County|FL072|Broward|12011|E|se|26.1257|-80.2706
FL|073|MFL|Inland Miami-Dade County|FL073|Miami-Dade|12086|E|se|25.6928|-80.6786
FL|074|MFL|Metropolitan Miami Dade|FL074|Miami-Dade|12086|E|se|25.7790|-80.3602
FL|075|MFL|Mainland Monroe|FL075|Mainland Monroe|12087|E|sw|25.5205|-81.0326
FL|168|MFL|Coastal Palm Beach County|FL168|Palm Beach|12099|E|se|26.7053|-80.0806
FL|172|MFL|Coastal Broward County|FL172|Broward|12011|E|se|26.1498|-80.1266
FL|173|MFL|Coastal Miami Dade County|FL173|Miami-Dade|12086|E|se|25.5815|-80.3117
FL|174|MFL|Far South Miami-Dade County|FL174|Miami-Dade|12086|E|se|25.299|-80.6497
CA|080|MFR|Western Siskiyou County|CA080|Siskiyou|06093|P|nn|41.5562|-123.1641
CA|081|MFR|Central Siskiyou County|CA081|Siskiyou|06093|P|nn|41.7362|-122.5631
CA|082|MFR|South Central Siskiyou County|CA082|Siskiyou|06093|P|nn|41.2704|-122.1846
CA|083|MFR|North Central and Southeast Siskiyou County|CA083|Siskiyou|06093|P|nn|41.5425|-121.8967
CA|084|MFR|Northeast Siskiyou and Northwest Modoc Counties|CA084|Modoc|06049|P|nn|41.8639|-121.6371
CA|084|MFR|Northeast Siskiyou and Northwest Modoc Counties|CA084|Siskiyou|06093|P|nn|41.8639|-121.6371
CA|085|MFR|Modoc County|CA085|Modoc|06049|P|nn|41.5611|-120.7585
OR|021|MFR|South Central Oregon Coast|OR021|Coos|41011|P|sw|43.181|-124.1567
OR|021|MFR|South Central Oregon Coast|OR021|Curry|41015|P|sw|43.181|-124.1567
OR|021|MFR|South Central Oregon Coast|OR021|Douglas|41019|P|sw|43.181|-124.1567
OR|022|MFR|Curry County Coast|OR022|Curry|41015|P|sw|42.342|-124.301
OR|023|MFR|Central Douglas County|OR023|Coos|41011|P|sw|43.2603|-123.4502
OR|023|MFR|Central Douglas County|OR023|Douglas|41019|P|sw|43.2603|-123.4502
OR|024|MFR|Eastern Curry County and Josephine County|OR024|Curry|41015|P|sw|42.3902|-123.7443
OR|024|MFR|Eastern Curry County and Josephine County|OR024|Josephine|41033|P|sw|42.3902|-123.7443
OR|025|MFR|Eastern Douglas County Foothills|OR025|Douglas|41019|P|sw|43.2384|-122.709
OR|026|MFR|Jackson County|OR026|Jackson|41029|P|sw|42.4652|-122.8457
OR|027|MFR|South Central Oregon Cascades|OR027|Douglas|41019|P|sw|43.1875|-122.1568
OR|027|MFR|South Central Oregon Cascades|OR027|Jackson|41029|P|sw|43.1875|-122.1568
OR|027|MFR|South Central Oregon Cascades|OR027|Klamath|41035|P|sc|43.1875|-122.1568
OR|028|MFR|Siskiyou Mountains and Southern Oregon Cascades|OR028|Jackson|41029|P|sw|42.3339|-122.4507
OR|028|MFR|Siskiyou Mountains and Southern Oregon Cascades|OR028|Josephine|41033|P|sw|42.3339|-122.4507
OR|028|MFR|Siskiyou Mountains and Southern Oregon Cascades|OR028|Klamath|41035|P|sc|42.3339|-122.4507
OR|029|MFR|Klamath Basin|OR029|Klamath|41035|P|sc|42.3505|-121.7222
OR|030|MFR|Northern and Eastern Klamath County and Western Lake County|OR030|Klamath|41035|P|sc|42.7799|-121.2476
OR|030|MFR|Northern and Eastern Klamath County and Western Lake County|OR030|Lake|41037|P|sc|42.7799|-121.2476
OR|031|MFR|Central and Eastern Lake County|OR031|Lake|41037|P|sc|42.8105|-120.2507
NC|029|MHX|Martin|NC029|Martin|37117|E|ee|35.8416|-77.1071
NC|044|MHX|Pitt|NC044|Pitt|37147|E|ee|35.5935|-77.3748
NC|045|MHX|Washington|NC045|Washington|37187|E|ee|35.8221|-76.5766
NC|046|MHX|Tyrrell|NC046|Tyrrell|37177|E|ee|35.8161|-76.2118
NC|047|MHX|Mainland Dare|NC047|Dare|37055|E|ee|35.7753|-75.8577
NC|079|MHX|Greene|NC079|Greene|37079|E|ee|35.4852|-77.6756
NC|080|MHX|Beaufort|NC080|Beaufort|37013|E|ee|35.4947|-76.8631
NC|081|MHX|Mainland Hyde|NC081|Hyde|37095|E|ee|35.5375|-76.2532
NC|090|MHX|Duplin|NC090|Duplin|37061|E|ee|34.9365|-77.9333
NC|091|MHX|Lenoir|NC091|Lenoir|37107|E|ee|35.2393|-77.6416
NC|092|MHX|Jones|NC092|Jones|37103|E|ee|35.0222|-77.3555
NC|094|MHX|Pamlico|NC094|Pamlico|37137|E|ee|35.1407|-76.7487
NC|193|MHX|Northern Craven|NC193|Craven|37049|E|ee|35.2508|-77.1891
NC|194|MHX|Southern Craven |NC194|Craven|37049|E|ee|34.9541|-76.9698
NC|195|MHX|West Carteret |NC195|Carteret|37031|E|ee|34.7672|-76.9068
NC|196|MHX|East Carteret |NC196|Carteret|37031|E|ee|34.8732|-76.5121
NC|198|MHX|Inland Onslow|NC198|Onslow|37133|E|ee|34.7775|-77.4736
NC|199|MHX|Coastal Onslow |NC199|Onslow|37133|E|ee|34.6161|-77.3148
NC|203|MHX|Northern Outer Banks |NC203|Dare|37055|E|ee|35.9623|-75.6658
NC|204|MHX|Ocracoke Island |NC204|Hyde|37095|E|ee|35.1283|-75.9146
NC|205|MHX|Hatteras Island |NC205|Dare|37055|E|ee|35.3945|-75.5413
WI|046|MKX|Marquette|WI046|Marquette|55077|C|sc|43.8196|-89.3988
WI|047|MKX|Green Lake|WI047|Green Lake|55047|C|sc|43.8003|-89.045
WI|051|MKX|Fond Du Lac|WI051|Fond du Lac|55039|C|ec|43.7536|-88.4882
WI|052|MKX|Sheboygan|WI052|Sheboygan|55117|C|ec|43.7212|-87.9454
WI|056|MKX|Sauk|WI056|Sauk|55111|C|sc|43.4268|-89.9484
WI|057|MKX|Columbia|WI057|Columbia|55021|C|sc|43.4665|-89.3338
WI|058|MKX|Dodge|WI058|Dodge|55027|C|se|43.4164|-88.7075
WI|059|MKX|Washington|WI059|Washington|55131|C|se|43.3684|-88.2308
WI|060|MKX|Ozaukee|WI060|Ozaukee|55089|C|se|43.3838|-87.9515
WI|062|MKX|Iowa|WI062|Iowa|55049|C|sc|43.0005|-90.1354
WI|063|MKX|Dane|WI063|Dane|55025|C|sc|43.0674|-89.4183
WI|064|MKX|Jefferson|WI064|Jefferson|55055|C|se|43.0209|-88.7759
WI|065|MKX|Waukesha|WI065|Waukesha|55133|C|se|43.0181|-88.3045
WI|066|MKX|Milwaukee|WI066|Milwaukee|55079|C|se|43.0071|-87.9667
WI|067|MKX|Lafayette|WI067|Lafayette|55065|C|sc|42.6605|-90.1317
WI|068|MKX|Green|WI068|Green|55045|C|sc|42.68|-89.6022
WI|069|MKX|Rock|WI069|Rock|55105|C|sc|42.6712|-89.0716
WI|070|MKX|Walworth|WI070|Walworth|55127|C|se|42.6685|-88.5419
WI|071|MKX|Racine|WI071|Racine|55101|C|se|42.7477|-88.0551
WI|072|MKX|Kenosha|WI072|Kenosha|55059|C|se|42.5767|-88.0418
FL|041|MLB|Inland Volusia County|FL041|Volusia|12127|E|ec|29.0622|-81.2756
FL|044|MLB|Northern Lake County|FL044|Lake|12069|E|ec|28.9313|-81.6301
FL|045|MLB|Orange|FL045|Orange|12095|E|ec|28.5148|-81.3238
FL|046|MLB|Seminole|FL046|Seminole|12117|E|ec|28.717|-81.2362
FL|053|MLB|Osceola|FL053|Osceola|12097|E|ec|28.0627|-81.1495
FL|058|MLB|Okeechobee|FL058|Okeechobee|12093|E|ec|27.4283|-80.9015
FL|141|MLB|Coastal Volusia County|FL141|Volusia|12127|E|ec|29.0562|-80.9907
FL|144|MLB|Southern Lake County|FL144|Lake|12069|E|ec|28.5634|-81.8061
FL|154|MLB|Coastal Indian River|FL154|Indian River|12061|E|ec|27.6872|-80.4549
FL|159|MLB|Coastal St. Lucie|FL159|St. Lucie|12111|E|ec|27.3965|-80.3424
FL|164|MLB|Coastal Martin|FL164|Martin|12085|E|ec|27.104|-80.2014
FL|247|MLB|Inland Northern Brevard|FL247|Brevard|12009|E|ec|28.6092|-80.9007
FL|254|MLB|Inland Indian River|FL254|Indian River|12061|E|ec|27.6955|-80.6904
FL|259|MLB|Inland St. Lucie|FL259|St. Lucie|12111|E|ec|27.3694|-80.5329
FL|264|MLB|Inland Martin|FL264|Martin|12085|E|ec|27.0779|-80.4514
FL|347|MLB|Mainland Northern Brevard|FL347|Brevard|12009|E|ec|28.5862|-80.8265
FL|447|MLB|Northern Brevard Barrier Islands|FL447|Brevard|12009|E|ec|28.5687|-80.6731
FL|547|MLB|Inland Southern Brevard|FL547|Brevard|12009|E|ec|28.0506|-80.7634
FL|647|MLB|Mainland Southern Brevard|FL647|Brevard|12009|E|ec|28.0939|-80.6434
FL|747|MLB|Southern Brevard Barrier Islands|FL747|Brevard|12009|E|ec|28.235|-80.6167
AL|051|MOB|Choctaw|AL051|Choctaw|01023|C|sw|32.0192|-88.2628
AL|052|MOB|Washington|AL052|Washington|01129|C|sw|31.4077|-88.2071
AL|053|MOB|Clarke|AL053|Clarke|01025|C|sw|31.6709|-87.8309
AL|054|MOB|Wilcox|AL054|Wilcox|01131|C|sc|31.9892|-87.3082
AL|055|MOB|Monroe|AL055|Monroe|01099|C|sc|31.5706|-87.3658
AL|056|MOB|Conecuh|AL056|Conecuh|01035|C|sc|31.4293|-86.9936
AL|057|MOB|Butler|AL057|Butler|01013|C|sc|31.7524|-86.6803
AL|058|MOB|Crenshaw|AL058|Crenshaw|01041|C|sc|31.7315|-86.3136
AL|059|MOB|Escambia|AL059|Escambia|01053|C|sc|31.1262|-87.1616
AL|060|MOB|Covington|AL060|Covington|01039|C|sc|31.2485|-86.4512
AL|261|MOB|Mobile Inland|AL261|Mobile|01097|C|sw|30.9237|-88.185
AL|262|MOB|Baldwin Inland|AL262|Baldwin|01003|C|sw|30.494|-87.6699
AL|263|MOB|Mobile Central|AL263|Mobile|01097|C|sw|30.5283|-88.2363
AL|264|MOB|Baldwin Central|AL264|Baldwin|01003|C|sw|30.9471|-87.7615
AL|265|MOB|Mobile Coastal|AL265|Mobile|01097|C|sw|30.5283|-88.2363
AL|266|MOB|Baldwin Coastal|AL266|Baldwin|01003|C|sw|30.494|-87.6699
FL|201|MOB|Escambia Inland|FL201|Escambia|12033|C|nw|30.8725|-87.4324
FL|202|MOB|Escambia Coastal|FL202|Escambia|12033|C|nw|30.51|-87.3166
FL|203|MOB|Santa Rosa Inland|FL203|Santa Rosa|12113|C|nw|30.8503|-87.036
FL|204|MOB|Santa Rosa Coastal|FL204|Santa Rosa|12113|C|nw|30.5786|-86.9928
FL|205|MOB|Okaloosa Inland|FL205|Okaloosa|12091|C|nw|30.8517|-86.5894
FL|206|MOB|Okaloosa Coastal|FL206|Okaloosa|12091|C|nw|30.563|-86.6034
MS|067|MOB|Wayne|MS067|Wayne|28153|C|se|31.6408|-88.6958
MS|075|MOB|Perry|MS075|Perry|28111|C|se|31.1721|-88.9923
MS|076|MOB|Greene|MS076|Greene|28041|C|se|31.2142|-88.6392
MS|078|MOB|Stone|MS078|Stone|28131|C|se|30.79|-89.1177
MS|079|MOB|George|MS079|George|28039|C|se|30.8626|-88.644
MN|041|MPX|Douglas|MN041|Douglas|27041|C|wc|45.9337|-95.4535
MN|042|MPX|Todd|MN042|Todd|27153|C|cc|46.0706|-94.8976
MN|043|MPX|Morrison|MN043|Morrison|27097|C|cc|46.0126|-94.2684
MN|044|MPX|Mille Lacs|MN044|Mille Lacs|27095|C|ec|45.938|-93.6301
MN|045|MPX|Kanabec|MN045|Kanabec|27065|C|ec|45.9453|-93.2935
MN|047|MPX|Stevens|MN047|Stevens|27149|C|wc|45.5861|-96.0003
MN|048|MPX|Pope|MN048|Pope|27121|C|wc|45.586|-95.4445
MN|049|MPX|Stearns|MN049|Stearns|27145|C|cc|45.5522|-94.613
MN|050|MPX|Benton|MN050|Benton|27009|C|cc|45.6991|-93.9989
MN|051|MPX|Sherburne|MN051|Sherburne|27141|C|cc|45.4439|-93.7745
MN|052|MPX|Isanti|MN052|Isanti|27059|C|ec|45.5615|-93.2952
MN|053|MPX|Chisago|MN053|Chisago|27025|C|ec|45.5025|-92.9083
MN|054|MPX|Lac Qui Parle|MN054|Lac qui Parle|27073|C|wc|44.9955|-96.1735
MN|055|MPX|Swift|MN055|Swift|27151|C|wc|45.2827|-95.6814
MN|056|MPX|Chippewa|MN056|Chippewa|27023|C|wc|45.0223|-95.5666
MN|057|MPX|Kandiyohi|MN057|Kandiyohi|27067|C|cc|45.1524|-95.0048
MN|058|MPX|Meeker|MN058|Meeker|27093|C|cc|45.1231|-94.5274
MN|059|MPX|Wright|MN059|Wright|27171|C|cc|45.1739|-93.963
MN|060|MPX|Hennepin|MN060|Hennepin|27053|C|ec|45.0045|-93.4768
MN|061|MPX|Anoka|MN061|Anoka|27003|C|ec|45.2732|-93.2464
MN|062|MPX|Ramsey|MN062|Ramsey|27123|C|ec|45.0171|-93.0994
MN|063|MPX|Washington|MN063|Washington|27163|C|ec|45.0383|-92.8839
MN|064|MPX|Yellow Medicine|MN064|Yellow Medicine|27173|C|wc|44.7162|-95.8683
MN|065|MPX|Renville|MN065|Renville|27129|C|cc|44.7268|-94.9472
MN|066|MPX|McLeod|MN066|McLeod|27085|C|cc|44.8235|-94.2724
MN|067|MPX|Sibley|MN067|Sibley|27143|C|cc|44.5795|-94.2321
MN|068|MPX|Carver|MN068|Carver|27019|C|ec|44.8208|-93.8025
MN|069|MPX|Scott|MN069|Scott|27139|C|ec|44.6484|-93.5357
MN|070|MPX|Dakota|MN070|Dakota|27037|C|ec|44.6718|-93.0656
MN|073|MPX|Redwood|MN073|Redwood|27127|C|sw|44.4037|-95.2539
MN|074|MPX|Brown|MN074|Brown|27015|C|sc|44.2421|-94.7277
MN|075|MPX|Nicollet|MN075|Nicollet|27103|C|sc|44.35|-94.2474
MN|076|MPX|Le Sueur|MN076|Le Sueur|27079|C|sc|44.3714|-93.73
MN|077|MPX|Rice|MN077|Rice|27131|C|sc|44.3541|-93.2966
MN|078|MPX|Goodhue|MN078|Goodhue|27049|C|se|44.4099|-92.7225
MN|082|MPX|Watonwan|MN082|Watonwan|27165|C|sc|43.9783|-94.6141
MN|083|MPX|Blue Earth|MN083|Blue Earth|27013|C|sc|44.0346|-94.0671
MN|084|MPX|Waseca|MN084|Waseca|27161|C|sc|44.0221|-93.5873
MN|085|MPX|Steele|MN085|Steele|27147|C|sc|44.0223|-93.226
MN|091|MPX|Martin|MN091|Martin|27091|C|sc|43.6742|-94.5511
MN|092|MPX|Faribault|MN092|Faribault|27043|C|sc|43.6739|-93.9479
MN|093|MPX|Freeborn|MN093|Freeborn|27047|C|sc|43.6738|-93.3489
WI|014|MPX|Polk|WI014|Polk|55095|C|nw|45.4614|-92.4414
WI|015|MPX|Barron|WI015|Barron|55005|C|nw|45.4238|-91.8484
WI|016|MPX|Rusk|WI016|Rusk|55107|C|nw|45.4751|-91.1331
WI|023|MPX|St. Croix|WI023|St. Croix|55109|C|wc|45.034|-92.4528
WI|024|MPX|Pierce|WI024|Pierce|55093|C|wc|44.7196|-92.4224
WI|025|MPX|Dunn|WI025|Dunn|55033|C|wc|44.9466|-91.8964
WI|026|MPX|Pepin|WI026|Pepin|55091|C|wc|44.5829|-92.0016
WI|027|MPX|Chippewa|WI027|Chippewa|55017|C|wc|45.0694|-91.2799
WI|028|MPX|Eau Claire|WI028|Eau Claire|55035|C|wc|44.7268|-91.286
MI|001|MQT|Keweenaw|MI001|Keweenaw|26083|E|wu|47.6027|-88.422
MI|002|MQT|Ontonagon|MI002|Ontonagon|26131|E|wu|46.6644|-89.315
MI|003|MQT|Houghton|MI003|Houghton|26061|E|wu|47.0531|-88.6207
MI|004|MQT|Baraga|MI004|Baraga|26013|E|nr|46.6626|-88.3652
MI|005|MQT|Marquette|MI005|Marquette|26103|E|nr|46.4314|-87.6415
MI|006|MQT|Alger|MI006|Alger|26003|E|nr|46.4099|-86.6019
MI|007|MQT|Luce|MI007|Luce|26095|E|eu|46.4707|-85.5443
MI|009|MQT|Gogebic|MI009|Gogebic|26053|C|wu|46.4089|-89.6944
MI|010|MQT|Iron|MI010|Iron|26071|C|sr|46.2087|-88.5306
MI|011|MQT|Dickinson|MI011|Dickinson|26043|C|sr|46.0091|-87.8704
MI|012|MQT|Menominee|MI012|Menominee|26109|C|sr|45.5792|-87.5573
MI|013|MQT|Delta|MI013|Delta|26041|E|sr|45.9197|-86.9244
MI|014|MQT|Southern Schoolcraft|MI014|Schoolcraft|26153|E|er|46.052|-86.1917
MI|084|MQT|Southern Houghton|MI084|Houghton|26061|E|wu|46.607|-88.8192
MI|085|MQT|Northern Schoolcraft|MI085|Schoolcraft|26153|E|er|46.3325|-86.2069
NC|060|MRX|Cherokee|NC060|Cherokee|37039|E|sw|35.1339|-84.0635
NC|061|MRX|Clay|NC061|Clay|37043|E|sw|35.0572|-83.7502
TN|012|MRX|Scott|TN012|Scott|47151|E|ea|36.4286|-84.5035
TN|013|MRX|Campbell|TN013|Campbell|47013|E|ea|36.4036|-84.1493
TN|014|MRX|Claiborne|TN014|Claiborne|47025|E|ea|36.4859|-83.6604
TN|015|MRX|Hancock|TN015|Hancock|47067|E|ea|36.5236|-83.2219
TN|016|MRX|Hawkins|TN016|Hawkins|47073|E|ea|36.4412|-82.9447
TN|017|MRX|Sullivan|TN017|Sullivan|47163|E|ea|36.5129|-82.3042
TN|018|MRX|Johnson|TN018|Johnson|47091|E|ea|36.4549|-81.8518
TN|035|MRX|Morgan|TN035|Morgan|47129|E|ea|36.135|-84.6491
TN|036|MRX|Anderson|TN036|Anderson|47001|E|ea|36.1184|-84.1985
TN|037|MRX|Union|TN037|Union|47173|E|ea|36.2879|-83.8375
TN|038|MRX|Grainger|TN038|Grainger|47057|E|ea|36.2762|-83.5096
TN|039|MRX|Hamblen|TN039|Hamblen|47063|E|ea|36.2172|-83.2666
TN|040|MRX|Northwest Cocke|TN040|Cocke|47029|E|ea|35.9835|-83.1536
TN|041|MRX|Cocke Smoky Mountains|TN041|Cocke|47029|E|ea|35.8417|-83.0743
TN|042|MRX|Northwest Greene|TN042|Greene|47059|E|ea|36.2009|-82.8533
TN|043|MRX|Southeast Greene|TN043|Greene|47059|E|ea|36.0126|-82.798
TN|044|MRX|Washington|TN044|Washington|47179|E|ea|36.2933|-82.4974
TN|045|MRX|Unicoi|TN045|Unicoi|47171|E|ea|36.1108|-82.4323
TN|046|MRX|Northwest Carter|TN046|Carter|47019|E|ea|36.3716|-82.1633
TN|047|MRX|Southeast Carter|TN047|Carter|47019|E|ea|36.2304|-82.099
TN|067|MRX|Roane|TN067|Roane|47145|E|ea|35.8478|-84.5233
TN|068|MRX|Loudon|TN068|Loudon|47105|E|ea|35.735|-84.3116
TN|069|MRX|Knox|TN069|Knox|47093|E|ea|35.9932|-83.9371
TN|070|MRX|Jefferson|TN070|Jefferson|47089|E|ea|36.051|-83.4463
TN|071|MRX|NW Blount|TN071|Blount|47009|E|ea|35.7251|-83.9604
TN|072|MRX|Blount Smoky Mountains|TN072|Blount|47009|E|ea|35.5851|-83.8315
TN|073|MRX|North Sevier|TN073|Sevier|47155|E|ea|35.8471|-83.5572
TN|074|MRX|Sevier Smoky Mountains|TN074|Sevier|47155|E|ea|35.6746|-83.4659
TN|081|MRX|Sequatchie|TN081|Sequatchie|47153|C|ea|35.3712|-85.4106
TN|082|MRX|Bledsoe|TN082|Bledsoe|47007|C|ea|35.5964|-85.2051
TN|083|MRX|Rhea|TN083|Rhea|47143|E|ea|35.6087|-84.9244
TN|084|MRX|Meigs|TN084|Meigs|47121|E|ea|35.5127|-84.8135
TN|085|MRX|McMinn|TN085|McMinn|47107|E|ea|35.4248|-84.6175
TN|086|MRX|Northwest Monroe|TN086|Monroe|47123|E|ea|35.4861|-84.3095
TN|087|MRX|Southeast Monroe|TN087|Monroe|47123|E|ea|35.353|-84.1353
TN|098|MRX|Marion|TN098|Marion|47115|C|ea|35.1294|-85.622
TN|099|MRX|Hamilton|TN099|Hamilton|47065|E|ea|35.1809|-85.1648
TN|100|MRX|Bradley|TN100|Bradley|47011|E|ea|35.1541|-84.8596
TN|101|MRX|West Polk|TN101|Polk|47139|E|ea|35.1416|-84.5937
TN|102|MRX|East Polk|TN102|Polk|47139|E|ea|35.0855|-84.4113
VA|001|MRX|Lee|VA001|Lee|51105|E|sw|36.7055|-83.1285
VA|002|MRX|Wise|VA002|Wise|51195|E|sw|36.9745|-82.6213
VA|002|MRX|Wise|VA002|City of Norton|51720|E|sw|36.9745|-82.6213
VA|005|MRX|Scott|VA005|Scott|51169|E|sw|36.7142|-82.603
VA|006|MRX|Russell|VA006|Russell|51167|E|sw|36.9338|-82.0956
VA|008|MRX|Washington|VA008|Washington|51191|E|sw|36.7221|-81.9642
VA|008|MRX|Washington|VA008|City of Bristol|51520|E|sw|36.7221|-81.9642
ID|005|MSO|Northern Clearwater Mountains|ID005|Clearwater|16035|P|nc|46.7138|-115.5769
ID|006|MSO|Southern Clearwater Mountains|ID006|Idaho|16049|MP|cc|45.8352|-115.2666
ID|007|MSO|Orofino/Grangeville Region|ID007|Clearwater|16035|MP|nc|46.2094|-116.0712
ID|007|MSO|Orofino/Grangeville Region|ID007|Idaho|16049|MP|cc|46.2094|-116.0712
ID|008|MSO|Lower Hells Canyon/Salmon River Region|ID008|Idaho|16049|MP|cc|45.6641|-116.4493
ID|009|MSO|Western Lemhi County|ID009|Lemhi|16059|M|ec|45.1209|-114.3901
ID|010|MSO|Eastern Lemhi County|ID010|Lemhi|16059|M|ec|44.8081|-113.5852
MT|001|MSO|Kootenai/Cabinet Region|MT001|Flathead|30029|M|nw|48.3391|-115.2165
MT|001|MSO|Kootenai/Cabinet Region|MT001|Lincoln|30053|M|nw|48.3391|-115.2165
MT|001|MSO|Kootenai/Cabinet Region|MT001|Sanders|30089|M|nw|48.3391|-115.2165
MT|002|MSO|West Glacier/Bob Marshall Region|MT002|Flathead|30029|M|nw|48.2755|-113.8037
MT|002|MSO|West Glacier/Bob Marshall Region|MT002|Lake|30047|M|nw|48.2755|-113.8037
MT|003|MSO|Flathead/Mission Valleys|MT003|Flathead|30029|M|nw|47.7732|-114.298
MT|003|MSO|Flathead/Mission Valleys|MT003|Lake|30047|M|nw|47.7732|-114.298
MT|003|MSO|Flathead/Mission Valleys|MT003|Sanders|30089|M|nw|47.7732|-114.298
MT|004|MSO|Lower Clark Fork Region|MT004|Mineral|30061|M|wc|47.3078|-115.0063
MT|004|MSO|Lower Clark Fork Region|MT004|Missoula|30063|M|wc|47.3078|-115.0063
MT|004|MSO|Lower Clark Fork Region|MT004|Sanders|30089|M|nw|47.3078|-115.0063
MT|005|MSO|Missoula/Bitterroot Valleys|MT005|Missoula|30063|M|wc|46.4888|-114.1079
MT|005|MSO|Missoula/Bitterroot Valleys|MT005|Ravalli|30081|M|wc|46.4888|-114.1079
MT|006|MSO|Bitterroot/Sapphire Mountains|MT006|Granite|30039|M|wc|46.1931|-113.9667
MT|006|MSO|Bitterroot/Sapphire Mountains|MT006|Missoula|30063|M|wc|46.1931|-113.9667
MT|006|MSO|Bitterroot/Sapphire Mountains|MT006|Ravalli|30081|M|wc|46.1931|-113.9667
MT|007|MSO|Butte/Pintlar Region|MT007|Deer Lodge|30023|M|wc|46.3886|-112.9185
MT|007|MSO|Butte/Pintlar Region|MT007|Granite|30039|M|wc|46.3886|-112.9185
MT|007|MSO|Butte/Pintlar Region|MT007|Powell|30077|M|wc|46.3886|-112.9185
MT|007|MSO|Butte/Pintlar Region|MT007|Silver Bow|30093|M|wc|46.3886|-112.9185
MT|043|MSO|Blackfoot Region|MT043|Granite|30039|M|wc|47.2005|-113.584
MT|043|MSO|Blackfoot Region|MT043|Lake|30047|M|nw|47.2005|-113.584
MT|043|MSO|Blackfoot Region|MT043|Missoula|30063|M|wc|47.2005|-113.584
MT|043|MSO|Blackfoot Region|MT043|Powell|30077|M|wc|47.2005|-113.584
CA|006|MTR|San Francisco|CA006|San Francisco|06075|P|ww|37.7558|-122.4423
CA|502|MTR|Marin Coastal Range|CA502|Marin|06041|P|ww|38.0602|-122.6859
CA|503|MTR|Sonoma Coastal Range|CA503|Sonoma|06097|P|ww|38.6598|-123.1621
CA|504|MTR|North Bay Interior Mountains|CA504|Napa|06055|P|ww|38.5823|-122.4433
CA|504|MTR|North Bay Interior Mountains|CA504|Sonoma|06097|P|ww|38.5823|-122.4433
CA|505|MTR|Coastal North Bay Including Point Reyes National Seashore|CA505|Marin|06041|P|ww|38.2364|-122.9543
CA|505|MTR|Coastal North Bay Including Point Reyes National Seashore|CA505|Sonoma|06097|P|ww|38.2364|-122.9543
CA|506|MTR|North Bay Interior Valleys|CA506|Marin|06041|P|ww|38.3698|-122.6419
CA|506|MTR|North Bay Interior Valleys|CA506|Napa|06055|P|ww|38.3698|-122.6419
CA|506|MTR|North Bay Interior Valleys|CA506|Sonoma|06097|P|ww|38.3698|-122.6419
CA|508|MTR|San Francisco Bay Shoreline|CA508|Alameda|06001|P|ww|37.5938|-122.165
CA|508|MTR|San Francisco Bay Shoreline|CA508|Contra Costa|06013|P|ww|37.5938|-122.165
CA|508|MTR|San Francisco Bay Shoreline|CA508|San Mateo|06081|P|ww|37.5938|-122.165
CA|508|MTR|San Francisco Bay Shoreline|CA508|Santa Clara|06085|P|ww|37.5938|-122.165
CA|509|MTR|San Fransisco Peninsula Coast|CA509|San Mateo|06081|P|ww|37.374|-122.3923
CA|509|MTR|San Fransisco Peninsula Coast|CA509|Santa Cruz|06087|P|ww|37.374|-122.3923
CA|510|MTR|East Bay Interior Valleys|CA510|Alameda|06001|P|ww|37.8803|-121.8801
CA|510|MTR|East Bay Interior Valleys|CA510|Contra Costa|06013|P|ww|37.8803|-121.8801
CA|512|MTR|Santa Cruz Mountains|CA512|San Mateo|06081|P|ww|37.1726|-122.04
CA|512|MTR|Santa Cruz Mountains|CA512|Santa Clara|06085|P|ww|37.1726|-122.04
CA|512|MTR|Santa Cruz Mountains|CA512|Santa Cruz|06087|P|ww|37.1726|-122.04
CA|513|MTR|Santa Clara Valley Including San Jose|CA513|Santa Clara|06085|P|ww|37.2196|-121.7971
CA|514|MTR|Eastern Santa Clara Hills|CA514|Santa Clara|06085|P|ww|37.243|-121.5277
CA|515|MTR|East Bay Hills|CA515|Alameda|06001|P|ww|37.7045|-121.8201
CA|515|MTR|East Bay Hills|CA515|Contra Costa|06013|P|ww|37.7045|-121.8201
CA|516|MTR|Southern Salinas Valley/Arroyo Seco and Lake San Antonio|CA516|Monterey|06053|P|ww|36.1014|-121.0546
CA|517|MTR|Santa Lucia Mountains and Los Padres National Forest|CA517|Monterey|06053|P|ww|36.1606|-121.4188
CA|518|MTR|Mountains Of San Benito County And Interior Monterey County Including Pinnacles National Monument|CA518|Monterey|06053|P|ww|36.3718|-120.9214
CA|518|MTR|Mountains Of San Benito County And Interior Monterey County Including Pinnacles National Monument|CA518|San Benito|06069|P|ww|36.3718|-120.9214
CA|528|MTR|Northern Salinas Valley/Hollister Valley and Carmel Valley|CA528|Monterey|06053|P|ww|36.6769|-121.5047
CA|528|MTR|Northern Salinas Valley/Hollister Valley and Carmel Valley|CA528|San Benito|06069|P|ww|36.6769|-121.5047
CA|529|MTR|Northern Monterey Bay|CA529|Santa Cruz|06087|P|ww|36.9757|-121.9005
CA|530|MTR|Southern Monterey Bay and Big Sur Coast|CA530|Monterey|06053|P|ww|36.6165|-121.7566
IA|043|OAX|Monona|IA043|Monona|19133|C|wc|42.0516|-95.96
IA|055|OAX|Harrison|IA055|Harrison|19085|C|sw|41.6829|-95.8167
IA|056|OAX|Shelby|IA056|Shelby|19165|C|sw|41.6851|-95.3103
IA|069|OAX|Pottawattamie|IA069|Pottawattamie|19155|C|sw|41.3364|-95.5423
IA|079|OAX|Mills|IA079|Mills|19129|C|sw|41.0332|-95.6214
IA|080|OAX|Montgomery|IA080|Montgomery|19137|C|sw|41.0301|-95.1563
IA|090|OAX|Fremont|IA090|Fremont|19071|C|sw|40.7456|-95.6047
IA|091|OAX|Page|IA091|Page|19145|C|sw|40.7391|-95.1502
NE|011|OAX|Knox|NE011|Knox|31107|C|ne|42.6369|-97.8919
NE|012|OAX|Cedar|NE012|Cedar|31027|C|ne|42.5993|-97.2523
NE|015|OAX|Thurston|NE015|Thurston|31173|C|ne|42.1582|-96.5441
NE|016|OAX|Antelope|NE016|Antelope|31003|C|ne|42.1769|-98.0667
NE|017|OAX|Pierce|NE017|Pierce|31139|C|ne|42.2644|-97.6013
NE|018|OAX|Wayne|NE018|Wayne|31179|C|ne|42.2092|-97.1193
NE|030|OAX|Boone|NE030|Boone|31011|C|ne|41.7068|-98.0673
NE|031|OAX|Madison|NE031|Madison|31119|C|ne|41.9166|-97.6008
NE|032|OAX|Stanton|NE032|Stanton|31167|C|ne|41.9168|-97.1939
NE|033|OAX|Cuming|NE033|Cuming|31039|C|ne|41.9164|-96.7874
NE|034|OAX|Burt|NE034|Burt|31021|C|ec|41.8515|-96.3287
NE|042|OAX|Platte|NE042|Platte|31141|C|ne|41.5701|-97.5198
NE|043|OAX|Colfax|NE043|Colfax|31037|C|ne|41.5731|-97.0867
NE|044|OAX|Dodge|NE044|Dodge|31053|C|ec|41.5777|-96.6542
NE|045|OAX|Washington|NE045|Washington|31177|C|ec|41.5311|-96.2218
NE|050|OAX|Butler|NE050|Butler|31023|C|ec|41.2242|-97.1306
NE|051|OAX|Saunders|NE051|Saunders|31155|C|ec|41.2261|-96.6373
NE|052|OAX|Douglas|NE052|Douglas|31055|C|ec|41.2953|-96.1544
NE|053|OAX|Sarpy|NE053|Sarpy|31153|C|ec|41.1131|-96.1119
NE|065|OAX|Seward|NE065|Seward|31159|C|se|40.8723|-97.1395
NE|066|OAX|Lancaster|NE066|Lancaster|31109|C|se|40.7841|-96.6878
NE|067|OAX|Cass|NE067|Cass|31025|C|se|40.9098|-96.1408
NE|068|OAX|Otoe|NE068|Otoe|31131|C|se|40.6485|-96.1348
NE|078|OAX|Saline|NE078|Saline|31151|C|se|40.524|-97.1408
NE|088|OAX|Jefferson|NE088|Jefferson|31095|C|se|40.1757|-97.1426
NE|089|OAX|Gage|NE089|Gage|31067|C|se|40.2619|-96.6893
NE|090|OAX|Johnson|NE090|Johnson|31097|C|se|40.3926|-96.2649
NE|091|OAX|Nemaha|NE091|Nemaha|31127|C|se|40.3881|-95.8486
NE|092|OAX|Pawnee|NE092|Pawnee|31133|C|se|40.1314|-96.237
NE|093|OAX|Richardson|NE093|Richardson|31147|C|se|40.1249|-95.7167
TN|005|OHX|Stewart|TN005|Stewart|47161|C|mi|36.5012|-87.8385
TN|006|OHX|Montgomery|TN006|Montgomery|47125|C|mi|36.4969|-87.3829
TN|007|OHX|Robertson|TN007|Robertson|47147|C|mi|36.5254|-86.8705
TN|008|OHX|Sumner|TN008|Sumner|47165|C|mi|36.4694|-86.4603
TN|009|OHX|Macon|TN009|Macon|47111|C|mi|36.532|-86.0072
TN|010|OHX|Clay|TN010|Clay|47027|C|mi|36.5511|-85.5438
TN|011|OHX|Pickett|TN011|Pickett|47137|C|mi|36.5585|-85.0748
TN|022|OHX|Benton|TN022|Benton|47005|C|mi|36.0698|-88.0683
TN|023|OHX|Houston|TN023|Houston|47083|C|mi|36.286|-87.7171
TN|024|OHX|Humphreys|TN024|Humphreys|47085|C|mi|36.0408|-87.7757
TN|025|OHX|Dickson|TN025|Dickson|47043|C|mi|36.1491|-87.3567
TN|026|OHX|Cheatham|TN026|Cheatham|47021|C|mi|36.2612|-87.0868
TN|027|OHX|Davidson|TN027|Davidson|47037|C|mi|36.1694|-86.7848
TN|028|OHX|Wilson|TN028|Wilson|47189|C|mi|36.1549|-86.2976
TN|029|OHX|Trousdale|TN029|Trousdale|47169|C|mi|36.3921|-86.1567
TN|030|OHX|Smith|TN030|Smith|47159|C|mi|36.2505|-85.9567
TN|031|OHX|Jackson|TN031|Jackson|47087|C|mi|36.3592|-85.6732
TN|032|OHX|Putnam|TN032|Putnam|47141|C|mi|36.1408|-85.4951
TN|033|OHX|Overton|TN033|Overton|47133|C|mi|36.345|-85.2881
TN|034|OHX|Fentress|TN034|Fentress|47049|C|mi|36.3805|-84.9324
TN|056|OHX|Perry|TN056|Perry|47135|C|mi|35.6426|-87.859
TN|057|OHX|Hickman|TN057|Hickman|47081|C|mi|35.8033|-87.4733
TN|058|OHX|Lewis|TN058|Lewis|47101|C|mi|35.5273|-87.4931
TN|059|OHX|Williamson|TN059|Williamson|47187|C|mi|35.8938|-86.8987
TN|060|OHX|Maury|TN060|Maury|47119|C|mi|35.617|-87.077
TN|061|OHX|Marshall|TN061|Marshall|47117|C|mi|35.4689|-86.7651
TN|062|OHX|Rutherford|TN062|Rutherford|47149|C|mi|35.8427|-86.4167
TN|063|OHX|Cannon|TN063|Cannon|47015|C|mi|35.8087|-86.0617
TN|064|OHX|De Kalb|TN064|De Kalb|47041|C|mi|35.9798|-85.8328
TN|065|OHX|White|TN065|White|47185|C|mi|35.9264|-85.4553
TN|066|OHX|Cumberland|TN066|Cumberland|47035|C|mi|35.9504|-84.9983
TN|075|OHX|Bedford|TN075|Bedford|47003|C|mi|35.5138|-86.4589
TN|077|OHX|Coffee|TN077|Coffee|47031|C|mi|35.4906|-86.0748
TN|078|OHX|Warren|TN078|Warren|47177|C|mi|35.6787|-85.7785
TN|079|OHX|Grundy|TN079|Grundy|47061|C|mi|35.3884|-85.7226
TN|080|OHX|Van Buren|TN080|Van Buren|47175|C|mi|35.696|-85.4525
TN|093|OHX|Wayne|TN093|Wayne|47181|C|mi|35.24|-87.788
TN|094|OHX|Lawrence|TN094|Lawrence|47099|C|mi|35.2173|-87.3956
TN|095|OHX|Giles|TN095|Giles|47055|C|mi|35.2022|-87.0348
CT|005|OKX|Northern Fairfield|CT005|Fairfield|09001|E|ss|41.353|-73.3629
CT|006|OKX|Northern New Haven|CT006|New Haven|09009|E|ss|41.4648|-72.9956
CT|007|OKX|Northern Middlesex|CT007|Middlesex|09007|E|ss|41.4977|-72.5551
CT|008|OKX|Northern New London|CT008|New London|09011|E|ss|41.5317|-72.0992
CT|009|OKX|Southern Fairfield|CT009|Fairfield|09001|E|ss|41.1301|-73.435
CT|010|OKX|Southern New Haven|CT010|New Haven|09009|E|ss|41.3108|-72.8154
CT|011|OKX|Southern Middlesex|CT011|Middlesex|09007|E|ss|41.3211|-72.4498
CT|012|OKX|Southern New London|CT012|New London|09011|E|ss|41.3615|-72.1034
NJ|002|OKX|Western Passaic|NJ002|Passaic|34031|E|ne|41.0934|-74.3518
NJ|004|OKX|Eastern Passaic|NJ004|Passaic|34031|E|ne|40.9176|-74.1999
NJ|006|OKX|Hudson|NJ006|Hudson|34017|E|ne|40.741|-74.0775
NJ|103|OKX|Western Bergen|NJ103|Bergen|34003|E|ne|41.0243|-74.1547
NJ|104|OKX|Eastern Bergen|NJ104|Bergen|34003|E|ne|40.9158|-74.0224
NJ|105|OKX|Western Essex|NJ105|Essex|34013|E|ne|40.8034|-74.2767
NJ|106|OKX|Eastern Essex|NJ106|Essex|34013|E|ne|40.7475|-74.1724
NJ|107|OKX|Western Union|NJ107|Eastern Union|34039|E|ne|40.6666|-74.3579
NJ|108|OKX|Eastern Union|NJ108|Eastern Union|34039|E|ne|40.6496|-74.2352
NY|067|OKX|Orange|NY067|Orange|36071|E|se|41.4022|-74.3056
NY|068|OKX|Putnam|NY068|Putnam|36079|E|se|41.4267|-73.7495
NY|069|OKX|Rockland|NY069|Rockland|36087|E|se|41.1529|-74.0241
NY|070|OKX|Northern Westchester|NY070|Westchester|36119|E|se|41.2221|-73.7474
NY|071|OKX|Southern Westchester|NY071|Westchester|36119|E|se|40.9833|-73.7799
NY|072|OKX|New York (Manhattan)|NY072|New York|36061|E|se|40.7786|-73.9665
NY|073|OKX|Bronx|NY073|Bronx|36005|E|se|40.8526|-73.8669
NY|074|OKX|Richmond (Staten Is.)|NY074|Richmond|36085|E|se|40.5802|-74.1557
NY|075|OKX|Kings (Brooklyn)|NY075|Kings|36047|E|se|40.6428|-73.9426
NY|078|OKX|Northwest Suffolk|NY078|Suffolk|36103|E|se|40.8778|-73.1715
NY|079|OKX|Northeast Suffolk|NY079|Suffolk|36103|E|se|40.9921|-72.5807
NY|080|OKX|Southwest Suffolk|NY080|Suffolk|36103|E|se|40.7503|-73.1828
NY|081|OKX|Southeast Suffolk|NY081|Suffolk|36103|E|se|40.9109|-72.4592
NY|176|OKX|Northern Queens|NY176|Queens|36081|E|se|40.748|-73.8438
NY|177|OKX|Northern Nassau|NY177|Nassau|36059|E|se|40.8335|-73.5976
NY|178|OKX|Southern Queens|NY178|Queens|36081|E|se|40.6648|-73.792
NY|179|OKX|Southern Nassau|NY179|Nassau|36059|E|se|40.6903|-73.5836
ID|001|OTX|Northern Panhandle|ID001|Bonner|16017|P|pa|48.4447|-116.5661
ID|001|OTX|Northern Panhandle|ID001|Boundary|16021|P|pa|48.4447|-116.5661
ID|001|OTX|Northern Panhandle|ID001|Kootenai|16055|P|pa|48.4447|-116.5661
ID|002|OTX|Coeur d'Alene Area|ID002|Kootenai|16055|P|pa|47.6003|-116.8182
ID|003|OTX|Idaho Palouse|ID003|Benewah|16009|P|pa|46.9308|-116.8785
ID|003|OTX|Idaho Palouse|ID003|Latah|16057|P|pa|46.9308|-116.8785
ID|004|OTX|Central Panhandle Mountains|ID004|Benewah|16009|P|pa|47.3003|-116.1291
ID|004|OTX|Central Panhandle Mountains|ID004|Kootenai|16055|P|pa|47.3003|-116.1291
ID|004|OTX|Central Panhandle Mountains|ID004|Latah|16057|P|pa|47.3003|-116.1291
ID|004|OTX|Central Panhandle Mountains|ID004|Shoshone|16079|P|pa|47.3003|-116.1291
ID|026|OTX|Lewiston Area|ID026|Nez Perce|16069|P|nc|46.4507|-116.7031
ID|027|OTX|Lewis and Southern Nez Perce Counties|ID027|Lewis|16061|P|nc|46.1926|-116.5889
ID|027|OTX|Lewis and Southern Nez Perce Counties|ID027|Nez Perce|16069|P|nc|46.1926|-116.5889
WA|031|OTX|Northeast Blue Mountains|WA031|Asotin|53003|P|se|46.1967|-117.3899
WA|031|OTX|Northeast Blue Mountains|WA031|Garfield|53023|P|se|46.1967|-117.3899
WA|032|OTX|Lower Garfield and Asotin Counties|WA032|Asotin|53003|P|se|46.422|-117.3795
WA|032|OTX|Lower Garfield and Asotin Counties|WA032|Garfield|53023|P|se|46.422|-117.3795
WA|033|OTX|Washington Palouse|WA033|Spokane|53063|P|ee|46.9272|-117.5068
WA|033|OTX|Washington Palouse|WA033|Whitman|53075|P|ee|46.9272|-117.5068
WA|034|OTX|Moses Lake Area|WA034|Adams|53001|P|ec|47.0108|-119.4918
WA|034|OTX|Moses Lake Area|WA034|Grant|53025|P|cc|47.0108|-119.4918
WA|035|OTX|Upper Columbia Basin|WA035|Adams|53001|P|ec|47.3555|-118.6116
WA|035|OTX|Upper Columbia Basin|WA035|Douglas|53017|P|nc|47.3555|-118.6116
WA|035|OTX|Upper Columbia Basin|WA035|Grant|53025|P|cc|47.3555|-118.6116
WA|035|OTX|Upper Columbia Basin|WA035|Lincoln|53043|P|ec|47.3555|-118.6116
WA|035|OTX|Upper Columbia Basin|WA035|Okanogan|53047|P|nc|47.3555|-118.6116
WA|036|OTX|Spokane Area|WA036|Lincoln|53043|P|ec|47.6181|-117.613
WA|036|OTX|Spokane Area|WA036|Spokane|53063|P|ee|47.6181|-117.613
WA|037|OTX|Northeast Mountains|WA037|Pend Oreille|53051|P|ne|48.4082|-117.6152
WA|037|OTX|Northeast Mountains|WA037|Spokane|53063|P|ee|48.4082|-117.6152
WA|037|OTX|Northeast Mountains|WA037|Stevens|53065|P|ne|48.4082|-117.6152
WA|038|OTX|Okanogan Highlands|WA038|Ferry|53019|P|ne|48.5329|-118.6987
WA|038|OTX|Okanogan Highlands|WA038|Okanogan|53047|P|nc|48.5329|-118.6987
WA|041|OTX|Wenatchee Area|WA041|Chelan|53007|P|nc|47.6296|-120.2222
WA|041|OTX|Wenatchee Area|WA041|Douglas|53017|P|nc|47.6296|-120.2222
WA|043|OTX|Okanogan Valley|WA043|Douglas|53017|P|nc|48.3496|-119.4519
WA|043|OTX|Okanogan Valley|WA043|Okanogan|53047|P|nc|48.3496|-119.4519
WA|044|OTX|Waterville Plateau|WA044|Douglas|53017|P|nc|47.6675|-119.6829
WA|044|OTX|Waterville Plateau|WA044|Grant|53025|P|cc|47.6675|-119.6829
WA|047|OTX|Central Chelan County|WA047|Chelan|53007|P|nc|47.8063|-120.5252
WA|048|OTX|Western Chelan County|WA048|Chelan|53007|P|nc|48.0304|-120.869
WA|049|OTX|Western Okanogan County|WA049|Okanogan|53047|P|nc|48.5981|-120.1638
OK|004|OUN|Harper|OK004|Harper|40059|C|nw|36.7887|-99.6673
OK|005|OUN|Woods|OK005|Woods|40151|C|nw|36.7669|-98.8651
OK|006|OUN|Alfalfa|OK006|Alfalfa|40003|C|nw|36.731|-98.324
OK|007|OUN|Grant|OK007|Grant|40053|C|nn|36.7962|-97.7861
OK|008|OUN|Kay|OK008|Kay|40071|C|nn|36.818|-97.1439
OK|009|OUN|Ellis|OK009|Ellis|40045|C|nw|36.2183|-99.7546
OK|010|OUN|Woodward|OK010|Woodward|40153|C|nw|36.4227|-99.265
OK|011|OUN|Major|OK011|Major|40093|C|nw|36.3116|-98.536
OK|012|OUN|Garfield|OK012|Garfield|40047|C|nn|36.379|-97.7828
OK|013|OUN|Noble|OK013|Noble|40103|C|nn|36.3886|-97.2306
OK|014|OUN|Roger Mills|OK014|Roger Mills|40129|C|ww|35.6883|-99.6957
OK|015|OUN|Dewey|OK015|Dewey|40043|C|nw|35.9877|-99.008
OK|016|OUN|Custer|OK016|Custer|40039|C|ww|35.6389|-99.0015
OK|017|OUN|Blaine|OK017|Blaine|40011|C|nw|35.8752|-98.4335
OK|018|OUN|Kingfisher|OK018|Kingfisher|40073|C|cc|35.9454|-97.9421
OK|019|OUN|Logan|OK019|Logan|40083|C|cc|35.9194|-97.4433
OK|020|OUN|Payne|OK020|Payne|40119|C|cc|36.0773|-96.9757
OK|021|OUN|Beckham|OK021|Beckham|40009|C|ww|35.2687|-99.682
OK|022|OUN|Washita|OK022|Washita|40149|C|ww|35.2904|-98.9923
OK|023|OUN|Caddo|OK023|Caddo|40015|C|sw|35.1744|-98.3751
OK|024|OUN|Canadian|OK024|Canadian|40017|C|cc|35.5425|-97.9825
OK|025|OUN|Oklahoma|OK025|Oklahoma|40109|C|cc|35.5515|-97.4072
OK|026|OUN|Lincoln|OK026|Lincoln|40081|C|cc|35.703|-96.8809
OK|027|OUN|Grady|OK027|Grady|40051|C|cc|35.017|-97.8841
OK|028|OUN|McClain|OK028|McClain|40087|C|cc|35.0087|-97.4436
OK|029|OUN|Cleveland|OK029|Cleveland|40027|C|cc|35.2036|-97.3271
OK|030|OUN|Pottawatomie|OK030|Pottawatomie|40125|C|cc|35.2068|-96.9483
OK|031|OUN|Seminole|OK031|Seminole|40133|C|ec|35.1675|-96.6156
OK|032|OUN|Hughes|OK032|Hughes|40063|C|se|35.0484|-96.2502
OK|033|OUN|Harmon|OK033|Harmon|40057|C|sw|34.7441|-99.8463
OK|034|OUN|Greer|OK034|Greer|40055|C|sw|34.9357|-99.5609
OK|035|OUN|Kiowa|OK035|Kiowa|40075|C|sw|34.9163|-98.9808
OK|036|OUN|Jackson|OK036|Jackson|40065|C|sw|34.588|-99.4147
OK|037|OUN|Tillman|OK037|Tillman|40141|C|sw|34.3728|-98.9242
OK|038|OUN|Comanche|OK038|Comanche|40031|C|sw|34.6621|-98.4717
OK|039|OUN|Stephens|OK039|Stephens|40137|C|ss|34.4856|-97.8514
OK|040|OUN|Garvin|OK040|Garvin|40049|C|ss|34.7045|-97.3093
OK|041|OUN|Murray|OK041|Murray|40099|C|ss|34.4823|-97.0679
OK|042|OUN|Pontotoc|OK042|Pontotoc|40123|C|ec|34.7281|-96.6844
OK|043|OUN|Coal|OK043|Coal|40029|C|se|34.5882|-96.2979
OK|044|OUN|Cotton|OK044|Cotton|40033|C|sw|34.2902|-98.3721
OK|045|OUN|Jefferson|OK045|Jefferson|40067|C|ss|34.1111|-97.8358
OK|046|OUN|Carter|OK046|Carter|40019|C|ss|34.2509|-97.2858
OK|047|OUN|Johnston|OK047|Johnston|40069|C|se|34.3165|-96.6606
OK|048|OUN|Atoka|OK048|Atoka|40005|C|se|34.3737|-96.0378
OK|050|OUN|Love|OK050|Love|40085|C|ss|33.9499|-97.2442
OK|051|OUN|Marshall|OK051|Marshall|40095|C|se|34.0245|-96.7691
OK|052|OUN|Bryan|OK052|Bryan|40013|C|se|33.9623|-96.26
TX|083|OUN|Hardeman|TX083|Hardeman|48197|C|nn|34.2903|-99.7457
TX|084|OUN|Foard|TX084|Foard|48155|C|nn|33.9746|-99.778
TX|085|OUN|Wilbarger|TX085|Wilbarger|48487|C|nn|34.0807|-99.241
TX|086|OUN|Wichita|TX086|Wichita|48485|C|nn|33.988|-98.7032
TX|087|OUN|Knox|TX087|Knox|48275|C|nn|33.6061|-99.7414
TX|088|OUN|Baylor|TX088|Baylor|48023|C|nn|33.6165|-99.2135
TX|089|OUN|Archer|TX089|Archer|48009|C|nn|33.6153|-98.6877
TX|090|OUN|Clay|TX090|Clay|48077|C|nn|33.7854|-98.2084
IL|075|PAH|Jefferson|IL075|Jefferson|17081|C|sc|38.3006|-88.924
IL|076|PAH|Wayne|IL076|Wayne|17191|C|sc|38.4295|-88.4256
IL|077|PAH|Edwards|IL077|Edwards|17047|C|se|38.4165|-88.0532
IL|078|PAH|Wabash|IL078|Wabash|17185|C|se|38.4461|-87.8443
IL|080|PAH|Perry|IL080|Perry|17145|C|sc|38.0838|-89.3671
IL|081|PAH|Franklin|IL081|Franklin|17055|C|sc|37.9923|-88.9242
IL|082|PAH|Hamilton|IL082|Hamilton|17065|C|sc|38.0816|-88.5392
IL|083|PAH|White|IL083|White|17193|C|se|38.0875|-88.1795
IL|084|PAH|Jackson|IL084|Jackson|17077|C|ss|37.7852|-89.3821
IL|085|PAH|Williamson|IL085|Williamson|17199|C|ss|37.7303|-88.9299
IL|086|PAH|Saline|IL086|Saline|17165|C|ss|37.7533|-88.5408
IL|087|PAH|Gallatin|IL087|Gallatin|17059|C|ss|37.7628|-88.2305
IL|088|PAH|Union|IL088|Union|17181|C|ss|37.4712|-89.2551
IL|089|PAH|Johnson|IL089|Johnson|17087|C|ss|37.4596|-88.8809
IL|090|PAH|Pope|IL090|Pope|17151|C|ss|37.4126|-88.5615
IL|091|PAH|Hardin|IL091|Hardin|17069|C|ss|37.5182|-88.2669
IL|092|PAH|Alexander|IL092|Alexander|17003|C|ss|37.1915|-89.3376
IL|093|PAH|Pulaski|IL093|Pulaski|17153|C|ss|37.2228|-89.1267
IL|094|PAH|Massac|IL094|Massac|17127|C|ss|37.219|-88.7078
IN|081|PAH|Gibson|IN081|Gibson|18051|C|sw|38.3118|-87.5846
IN|082|PAH|Pike|IN082|Pike|18125|C|sw|38.3988|-87.2322
IN|085|PAH|Posey|IN085|Posey|18129|C|sw|38.0218|-87.8684
IN|086|PAH|Vanderburgh|IN086|Vanderburgh|18163|C|sw|38.0254|-87.5857
IN|087|PAH|Warrick|IN087|Warrick|18173|C|sw|38.0922|-87.2721
IN|088|PAH|Spencer|IN088|Spencer|18147|C|sw|38.0142|-87.0077
KY|001|PAH|Fulton|KY001|Fulton|21075|C|ww|36.5541|-89.1873
KY|002|PAH|Hickman|KY002|Hickman|21105|C|ww|36.6781|-88.9761
KY|003|PAH|Carlisle|KY003|Carlisle|21039|C|ww|36.8532|-88.9709
KY|004|PAH|Ballard|KY004|Ballard|21007|C|ww|37.0584|-88.9992
KY|005|PAH|McCracken|KY005|McCracken|21145|C|ww|37.0539|-88.7127
KY|006|PAH|Graves|KY006|Graves|21083|C|ww|36.723|-88.6512
KY|007|PAH|Livingston|KY007|Livingston|21139|C|ww|37.2097|-88.3536
KY|008|PAH|Marshall|KY008|Marshall|21157|C|ww|36.8834|-88.3293
KY|009|PAH|Calloway|KY009|Calloway|21035|C|ww|36.6211|-88.2723
KY|010|PAH|Crittenden|KY010|Crittenden|21055|C|ww|37.3527|-88.0972
KY|011|PAH|Lyon|KY011|Lyon|21143|C|ww|37.0191|-88.0832
KY|012|PAH|Trigg|KY012|Trigg|21221|C|ww|36.8064|-87.8734
KY|013|PAH|Caldwell|KY013|Caldwell|21033|C|ww|37.1453|-87.8679
KY|014|PAH|Union|KY014|Union|21225|C|nw|37.6584|-87.9453
KY|015|PAH|Webster|KY015|Webster|21233|C|nw|37.5183|-87.6832
KY|016|PAH|Hopkins|KY016|Hopkins|21107|C|nw|37.3088|-87.5409
KY|017|PAH|Christian|KY017|Christian|21047|C|sc|36.8941|-87.4904
KY|018|PAH|Henderson|KY018|Henderson|21101|C|nw|37.7961|-87.5729
KY|019|PAH|Daviess|KY019|Daviess|21059|C|nw|37.7318|-87.0873
KY|020|PAH|McLean|KY020|McLean|21149|C|nw|37.5291|-87.2636
KY|021|PAH|Muhlenberg|KY021|Muhlenberg|21177|C|sc|37.2157|-87.1421
KY|022|PAH|Todd|KY022|Todd|21219|C|sc|36.8356|-87.1791
MO|076|PAH|Perry|MO076|Perry|29157|C|se|37.7071|-89.8244
MO|086|PAH|Bollinger|MO086|Bollinger|29017|C|se|37.3222|-90.0259
MO|087|PAH|Cape Girardeau|MO087|Cape Girardeau|29031|C|se|37.3839|-89.6845
MO|100|PAH|Wayne|MO100|Wayne|29223|C|se|37.1126|-90.4614
MO|107|PAH|Carter|MO107|Carter|29035|C|se|36.9413|-90.9623
MO|108|PAH|Ripley|MO108|Ripley|29181|C|se|36.6528|-90.8639
MO|109|PAH|Butler|MO109|Butler|29023|C|se|36.7164|-90.4065
MO|110|PAH|Stoddard|MO110|Stoddard|29207|C|se|36.8555|-89.9444
MO|111|PAH|Scott|MO111|Scott|29201|C|se|37.053|-89.5686
MO|112|PAH|Mississippi|MO112|Mississippi|29133|C|se|36.8281|-89.2911
MO|114|PAH|New Madrid|MO114|New Madrid|29143|C|se|36.5942|-89.6516
OH|039|PBZ|Tuscarawas|OH039|Tuscarawas|39157|E|ec|40.441|-81.4738
OH|040|PBZ|Carroll|OH040|Carroll|39019|E|ec|40.5796|-81.0897
OH|041|PBZ|Columbiana|OH041|Columbiana|39029|E|ec|40.7686|-80.7775
OH|048|PBZ|Coshocton|OH048|Coshocton|39031|E|ec|40.3016|-81.92
OH|049|PBZ|Harrison|OH049|Harrison|39067|E|ec|40.2938|-81.0911
OH|050|PBZ|Jefferson|OH050|Jefferson|39081|E|ec|40.385|-80.761
OH|057|PBZ|Muskingum|OH057|Muskingum|39119|E|ec|39.9654|-81.9444
OH|058|PBZ|Guernsey|OH058|Guernsey|39059|E|ec|40.0521|-81.4942
OH|059|PBZ|Belmont|OH059|Belmont|39013|E|ec|40.0158|-80.9885
OH|068|PBZ|Noble|OH068|Noble|39121|E|ec|39.766|-81.4555
OH|069|PBZ|Monroe|OH069|Monroe|39111|E|ec|39.7274|-81.0829
PA|007|PBZ|Mercer|PA007|Mercer|42085|E|nw|41.3022|-80.2577
PA|008|PBZ|Venango|PA008|Venango|42121|E|nw|41.401|-79.758
PA|009|PBZ|Forest|PA009|Forest|42053|E|nw|41.5132|-79.2361
PA|013|PBZ|Lawrence|PA013|Lawrence|42073|E|ww|40.9912|-80.3342
PA|014|PBZ|Butler|PA014|Butler|42019|E|wc|40.9117|-79.913
PA|015|PBZ|Clarion|PA015|Clarion|42031|E|wc|41.1925|-79.421
PA|016|PBZ|Jefferson|PA016|Jefferson|42065|E|wc|41.1281|-78.9995
PA|020|PBZ|Beaver|PA020|Beaver|42007|E|ww|40.6823|-80.3493
PA|021|PBZ|Allegheny|PA021|Allegheny|42003|E|sw|40.4688|-79.9812
PA|022|PBZ|Armstrong|PA022|Armstrong|42005|E|wc|40.8125|-79.4645
PA|029|PBZ|Washington|PA029|Washington|42125|E|sw|40.1894|-80.2482
PA|031|PBZ|Greene|PA031|Greene|42059|E|sw|39.8538|-80.2229
PA|073|PBZ|Westmoreland|PA073|Westmoreland|42129|E|sw|40.3446|-79.5748
PA|074|PBZ|Westmoreland Ridges|PA074|Westmoreland|42129|E|sw|40.2371|-79.2326
PA|075|PBZ|Fayette|PA075|Fayette|42051|E|sw|39.9485|-79.7718
PA|076|PBZ|Fayette Ridges|PA076|Fayette|42051|E|sw|39.8896|-79.5165
PA|077|PBZ|Indiana|PA077|Indiana|42063|E|wc|40.6974|-79.1167
PA|078|PBZ|Higher Elevations of Indiana|PA078|Indiana|42063|E|wc|40.5318|-79.0103
WV|001|PBZ|Hancock|WV001|Hancock|54029|E|nn|40.5213|-80.5739
WV|002|PBZ|Brooke|WV002|Brooke|54009|E|nn|40.2733|-80.5765
WV|003|PBZ|Ohio|WV003|Ohio|54069|E|nn|40.0969|-80.6189
WV|004|PBZ|Marshall|WV004|Marshall|54051|E|nn|39.8606|-80.6634
WV|012|PBZ|Wetzel|WV012|Wetzel|54103|E|nn|39.6053|-80.6391
WV|021|PBZ|Marion|WV021|Marion|54049|E|nn|39.51|-80.2434
WV|509|PBZ|Monongalia|WV509|Monongalia|54061|E|nn|39.6303|-80.0465
WV|510|PBZ|Ridges of Eastern Monongalia and Northwestern Preston|WV510|Monongalia|54061|E|nn|39.6303|-80.0465
WV|511|PBZ|Preston|WV511|Preston|54077|E|nn|39.4693|-79.6681
WV|512|PBZ|Eastern Preston|WV512|Preston|54077|E|nn|39.4693|-79.6681
WV|513|PBZ|Western Tucker|WV513|Tucker|54093|E|nn|39.1136|-79.565
WV|514|PBZ|Eastern Tucker|WV514|Tucker|54093|E|nn|39.1136|-79.565
OR|015|PDT|Western Columbia River Gorge|OR015|Hood River|41027|P|cc|45.5872|-122.0526
OR|015|PDT|Western Columbia River Gorge|OR015|Multnomah|41051|P|cc|45.5872|-122.0526
OR|016|PDT|Central Columbia River Gorge|OR016|Hood River|41031|P|cc|45.6845|-121.6091
OR|041|PDT|East Columbia River Gorge|OR041|Gilliam|41021|P|nc|45.646|-120.5512
OR|041|PDT|East Columbia River Gorge|OR041|Sherman|41055|P|nc|45.646|-120.5512
OR|041|PDT|East Columbia River Gorge|OR041|Wasco|41065|P|nc|45.646|-120.5512
OR|044|PDT|Lower Columbia Basin of Oregon|OR044|Morrow|41049|P|ne|45.7453|-119.4683
OR|044|PDT|Lower Columbia Basin of Oregon|OR044|Umatilla|41059|P|ne|45.7453|-119.4683
OR|049|PDT|Grande Ronde Valley|OR049|Union|41061|P|ne|45.3737|-117.9515
OR|050|PDT|Wallowa County|OR050|Union|41061|P|ne|45.4827|-117.1835
OR|050|PDT|Wallowa County|OR050|Wallowa|41063|P|ne|45.4827|-117.1835
OR|502|PDT|Northern Blue Mountains of Oregon|OR502|Umatilla|41059|P|ne|45.6952|-118.0041
OR|502|PDT|Northern Blue Mountains of Oregon|OR502|Union|41061|P|ne|45.6952|-118.0041
OR|502|PDT|Northern Blue Mountains of Oregon|OR502|Wallowa|41063|P|ne|45.6952|-118.0041
OR|503|PDT|Southern Blue Mountains of Oregon|OR503|Gilliam|41021|P|nc|44.9813|-118.9718
OR|503|PDT|Southern Blue Mountains of Oregon|OR503|Grant|41023|P|ec|44.9813|-118.9718
OR|503|PDT|Southern Blue Mountains of Oregon|OR503|Morrow|41049|P|ne|44.9813|-118.9718
OR|503|PDT|Southern Blue Mountains of Oregon|OR503|Umatilla|41059|P|ne|44.9813|-118.9718
OR|503|PDT|Southern Blue Mountains of Oregon|OR503|Union|41061|P|ne|44.9813|-118.9718
OR|503|PDT|Southern Blue Mountains of Oregon|OR503|Wheeler|41069|P|cc|44.9813|-118.9718
OR|505|PDT|John Day Basin|OR505|Grant|41023|P|ec|44.7315|-119.7825
OR|505|PDT|John Day Basin|OR505|Jefferson|41031|P|cc|44.7315|-119.7825
OR|505|PDT|John Day Basin|OR505|Morrow|41049|P|ne|44.7315|-119.7825
OR|505|PDT|John Day Basin|OR505|Wasco|41065|P|nc|44.7315|-119.7825
OR|505|PDT|John Day Basin|OR505|Wheeler|41069|P|cc|44.7315|-119.7825
OR|506|PDT|Ochoco-John Day Highlands|OR506|Crook|41013|P|cc|44.1652|-120.0086
OR|506|PDT|Ochoco-John Day Highlands|OR506|Deschutes|41017|P|cc|44.1652|-120.0086
OR|506|PDT|Ochoco-John Day Highlands|OR506|Grant|41023|P|ec|44.1652|-120.0086
OR|506|PDT|Ochoco-John Day Highlands|OR506|Jefferson|41031|P|cc|44.1652|-120.0086
OR|506|PDT|Ochoco-John Day Highlands|OR506|Wheeler|41069|P|cc|44.1652|-120.0086
OR|507|PDT|Foothills of the Northern Blue Mountains of Oregon|OR507|Umatilla|41059|P|ne|45.7238|-118.7135
OR|508|PDT|Foothills of the Southern Blue Mountains of Oregon|OR508|Gilliam|41021|P|nc|45.3442|-120.0029
OR|508|PDT|Foothills of the Southern Blue Mountains of Oregon|OR508|Morrow|41049|P|ne|45.3442|-120.0029
OR|508|PDT|Foothills of the Southern Blue Mountains of Oregon|OR508|Wheeler|41069|P|cc|45.3442|-120.0029
OR|509|PDT|East Slopes of the Oregon Cascades|OR509|Deschutes|41017|P|cc|44.2627|-121.5516
OR|509|PDT|East Slopes of the Oregon Cascades|OR509|Jefferson|41031|P|cc|44.2627|-121.5516
OR|509|PDT|East Slopes of the Oregon Cascades|OR509|Wasco|41065|P|nc|44.2627|-121.5516
OR|510|PDT|North Central Oregon|OR510|Sherman|41055|P|nc|45.221|-121.0222
OR|510|PDT|North Central Oregon|OR510|Wasco|41065|P|nc|45.221|-121.0222
OR|511|PDT|Central Oregon|OR511|Crook|41013|P|cc|44.4439|-121.1488
OR|511|PDT|Central Oregon|OR511|Deschutes|41017|P|cc|44.4439|-121.1488
OR|511|PDT|Central Oregon|OR511|Jefferson|41031|P|cc|44.4439|-121.1488
WA|522|PDT|Upper Slopes of the Eastern Washington Cascades Crest|WA522|Kittitas|53037|P|cc|46.9379|-121.2667
WA|522|PDT|Upper Slopes of the Eastern Washington Cascades Crest|WA522|Yakima|53077|P|sc|46.9379|-121.2667
WA|523|PDT|Lower Slopes of the Eastern Washington Cascades Crest|WA523|Kittitas|53037|P|cc|46.4569|-120.7387
WA|523|PDT|Lower Slopes of the Eastern Washington Cascades Crest|WA523|Klickitat|53039|P|cc|46.4569|-120.7387
WA|523|PDT|Lower Slopes of the Eastern Washington Cascades Crest|WA523|Yakima|53077|P|sc|46.4569|-120.7387
WA|024|PDT|Eastern Columbia River Gorge of Washington|WA024|Klickitat|53039|P|cc|45.7233|-120.8763
WA|026|PDT|Kittitas Valley|WA026|Kittitas|53037|P|cc|46.9429|-120.314
WA|026|PDT|Kittitas Valley|WA026|Yakima|53077|P|sc|46.9429|-120.314
WA|027|PDT|Yakima Valley|WA027|Yakima|53077|P|sc|46.4331|-120.312
WA|028|PDT|Lower Columbia Basin of Washington|WA028|Benton|53005|P|sc|46.3373|-119.1824
WA|028|PDT|Lower Columbia Basin of Washington|WA028|Franklin|53021|P|sc|46.3373|-119.1824
WA|028|PDT|Lower Columbia Basin of Washington|WA028|Klickitat|53039|P|cc|46.3373|-119.1824
WA|028|PDT|Lower Columbia Basin of Washington|WA028|Walla Walla|53071|P|sc|46.3373|-119.1824
WA|029|PDT|Foothills of the Blue Mountains of Washington|WA029|Columbia|53013|P|se|46.3118|-118.2123
WA|029|PDT|Foothills of the Blue Mountains of Washington|WA029|Walla Walla|53071|P|sc|46.3118|-118.2123
WA|030|PDT|Northwest Blue Mountains|WA030|Columbia|53013|P|se|46.1508|-117.8128
WA|030|PDT|Northwest Blue Mountains|WA030|Walla Walla|53071|P|sc|46.1508|-117.8128
WA|521|PDT|Simcoe Highlands|WA521|Klickitat|53039|P|cc|45.9735|-120.6525
WA|521|PDT|Simcoe Highlands|WA521|Yakima|53077|P|sc|45.9735|-120.6525
DE|001|PHI|New Castle|DE001|New Castle|10003|E|nn|39.581|-75.6489
DE|002|PHI|Kent|DE002|Kent|10001|E|cc|39.0867|-75.5688
DE|003|PHI|Inland Sussex|DE003|Sussex|10005|E|cc|38.6653|-75.4181
DE|004|PHI|Delaware Beaches|DE004|Sussex|10005|E|cc|38.6114|-75.0919
MD|012|PHI|Kent|MD012|Kent|24029|E|ne|39.1797|-76.116
MD|012|PHI|Kent|MD012|Kent|24029|E|ne|39.2574|-76.0362
MD|015|PHI|Queen Anne's|MD015|Queen Anne's|24035|E|ne|39.0705|-76.0196
MD|015|PHI|Queen Anne's|MD015|Queen Anne's|24035|E|ne|39.0705|-76.0196
MD|019|PHI|Talbot|MD019|Talbot|24041|E|ee|38.7739|-76.0928
MD|020|PHI|Caroline|MD020|Caroline|24011|E|ee|38.8717|-75.8317
NJ|001|PHI|Sussex|NJ001|Sussex|34037|E|nw|41.1394|-74.6902
NJ|007|PHI|Warren|NJ007|Warren|34041|E|nw|40.8574|-74.997
NJ|008|PHI|Morris|NJ008|Morris|34027|E|nn|40.8621|-74.5445
NJ|009|PHI|Hunterdon|NJ009|Hunterdon|34019|E|nw|40.5672|-74.9123
NJ|010|PHI|Somerset|NJ010|Somerset|34035|E|nn|40.5637|-74.6163
NJ|012|PHI|Middlesex|NJ012|Middlesex|34023|E|nn|40.4394|-74.4113
NJ|013|PHI|Western Monmouth|NJ013|Monmouth|34025|E|cc|40.2596|-74.2614
NJ|014|PHI|Eastern Monmouth|NJ014|Monmouth|34025|E|cc|40.2557|-74.0295
NJ|015|PHI|Mercer|NJ015|Mercer|34021|E|cc|40.2833|-74.7015
NJ|016|PHI|Salem|NJ016|Salem|34033|E|ss|39.5872|-75.3459
NJ|017|PHI|Gloucester|NJ017|Gloucester|34015|E|ss|39.7173|-75.1419
NJ|018|PHI|Camden|NJ018|Camden|34007|E|ss|39.8038|-74.9599
NJ|019|PHI|Northwestern Burlington|NJ019|Burlington|34005|E|ss|39.985|-74.7572
NJ|020|PHI|Ocean|NJ020|Ocean|34029|E|ss|39.9191|-74.3099
NJ|021|PHI|Cumberland|NJ021|Cumberland|34011|E|ss|39.3735|-75.1099
NJ|022|PHI|Atlantic|NJ022|Atlantic|34001|E|ss|39.4906|-74.6976
NJ|023|PHI|Cape May|NJ023|Cape May|34009|E|ss|39.1768|-74.8227
NJ|024|PHI|Atlantic Coastal Cape May|NJ024|Cape May|34009|E|ss|39.0952|-74.7718
NJ|025|PHI|Coastal Atlantic|NJ025|Atlantic|34001|E|ss|39.393|-74.4448
NJ|026|PHI|Coastal Ocean|NJ026|Ocean|34029|E|ss|39.789|-74.1647
NJ|027|PHI|Southeastern Burlington|NJ027|Burlington|34005|E|ss|39.7478|-74.5605
PA|054|PHI|Carbon|PA054|Carbon|42025|E|ne|40.9183|-75.7088
PA|055|PHI|Monroe|PA055|Monroe|42089|E|ne|41.0582|-75.3394
PA|060|PHI|Berks|PA060|Berks|42011|E|ee|40.4164|-75.926
PA|061|PHI|Lehigh|PA061|Lehigh|42077|E|ee|40.6129|-75.5924
PA|062|PHI|Northampton|PA062|Northampton|42095|E|ee|40.7543|-75.3074
PA|070|PHI|Delaware|PA070|Delaware|42045|E|se|39.9167|-75.399
PA|071|PHI|Philadelphia|PA071|Philadelphia|42101|E|se|40.0076|-75.1338
PA|101|PHI|Western Chester|PA101|Chester|42029|E|se|39.9733|-75.7483
PA|102|PHI|Eastern Chester|PA102|Chester|42029|E|se|39.9733|-75.7483
PA|103|PHI|Western Montgomery|PA103|Montgomery|42091|E|se|40.2109|-75.3672
PA|104|PHI|Eastern Montgomery|PA104|Montgomery|42091|E|se|40.2109|-75.3672
PA|105|PHI|Bucks|PA105|Upper Bucks|42017|E|se|40.337|-75.1067
PA|106|PHI|Bucks|PA106|Lower Bucks|42017|E|se|40.337|-75.1067
ID|051|PIH|Shoshone/Lava Beds|ID051|Blaine|16013|M|se|43.0804|-113.8956
ID|051|PIH|Shoshone/Lava Beds|ID051|Lincoln|16063|M|se|43.0804|-113.8956
ID|051|PIH|Shoshone/Lava Beds|ID051|Minidoka|16067|M|se|43.0804|-113.8956
ID|052|PIH|Arco/Mud Lake Desert|ID052|Bingham|16011|M|se|43.6353|-112.7958
ID|052|PIH|Arco/Mud Lake Desert|ID052|Bonneville|16019|M|se|43.6353|-112.7958
ID|052|PIH|Arco/Mud Lake Desert|ID052|Butte|16023|M|se|43.6353|-112.7958
ID|052|PIH|Arco/Mud Lake Desert|ID052|Jefferson|16051|M|se|43.6353|-112.7958
ID|053|PIH|Upper Snake River Plain|ID053|Bonneville|16019|M|se|43.7916|-111.9224
ID|053|PIH|Upper Snake River Plain|ID053|Fremont|16043|M|se|43.7916|-111.9224
ID|053|PIH|Upper Snake River Plain|ID053|Jefferson|16051|M|se|43.7916|-111.9224
ID|053|PIH|Upper Snake River Plain|ID053|Madison|16065|M|se|43.7916|-111.9224
ID|054|PIH|Lower Snake River Plain|ID054|Bannock|16005|M|se|43.1242|-112.6045
ID|054|PIH|Lower Snake River Plain|ID054|Bingham|16011|M|se|43.1242|-112.6045
ID|054|PIH|Lower Snake River Plain|ID054|Power|16077|M|se|43.1242|-112.6045
ID|055|PIH|Eastern Magic Valley|ID055|Blaine|16013|M|se|42.7002|-113.4605
ID|055|PIH|Eastern Magic Valley|ID055|Cassia|16031|M|se|42.7002|-113.4605
ID|055|PIH|Eastern Magic Valley|ID055|Minidoka|16067|M|se|42.7002|-113.4605
ID|055|PIH|Eastern Magic Valley|ID055|Power|16077|M|se|42.7002|-113.4605
ID|056|PIH|Southern Hills/Albion Mountains|ID056|Cassia|16031|M|se|42.1932|-113.8364
ID|057|PIH|Raft River Region|ID057|Cassia|16031|M|se|42.2756|-113.0516
ID|057|PIH|Raft River Region|ID057|Oneida|16071|M|se|42.2756|-113.0516
ID|057|PIH|Raft River Region|ID057|Power|16077|M|se|42.2756|-113.0516
ID|058|PIH|Marsh and Arbon Highlands|ID058|Bannock|16005|M|se|42.6797|-112.2919
ID|058|PIH|Marsh and Arbon Highlands|ID058|Bingham|16011|M|se|42.6797|-112.2919
ID|058|PIH|Marsh and Arbon Highlands|ID058|Caribou|16029|M|se|42.6797|-112.2919
ID|058|PIH|Marsh and Arbon Highlands|ID058|Power|16077|M|se|42.6797|-112.2919
ID|059|PIH|Franklin/Eastern Oneida Region|ID059|Franklin|16041|M|se|42.2039|-112.1984
ID|059|PIH|Franklin/Eastern Oneida Region|ID059|Oneida|16071|M|se|42.2039|-112.1984
ID|060|PIH|Bear River Range|ID060|Bear Lake|16007|M|se|42.2521|-111.5742
ID|060|PIH|Bear River Range|ID060|Caribou|16029|M|se|42.2521|-111.5742
ID|060|PIH|Bear River Range|ID060|Franklin|16041|M|se|42.2521|-111.5742
ID|061|PIH|Bear Lake Valley|ID061|Bear Lake|16007|M|se|42.2447|-111.2738
ID|062|PIH|Blackfoot Mountains|ID062|Bingham|16011|M|se|42.9895|-111.747
ID|062|PIH|Blackfoot Mountains|ID062|Bonneville|16019|M|se|42.9895|-111.747
ID|062|PIH|Blackfoot Mountains|ID062|Caribou|16029|M|se|42.9895|-111.747
ID|063|PIH|Caribou Range|ID063|Bear Lake|16007|M|se|42.9919|-111.2925
ID|063|PIH|Caribou Range|ID063|Bonneville|16019|M|se|42.9919|-111.2925
ID|063|PIH|Caribou Range|ID063|Caribou|16029|M|se|42.9919|-111.2925
ID|064|PIH|Big Hole Mountains|ID064|Bonneville|16019|M|ee|43.6154|-111.2986
ID|064|PIH|Big Hole Mountains|ID064|Madison|16065|M|ee|43.6154|-111.2986
ID|064|PIH|Big Hole Mountains|ID064|Teton|16081|M|ee|43.6154|-111.2986
ID|065|PIH|Teton Valley|ID065|Fremont|16043|M|ee|43.8893|-111.2616
ID|065|PIH|Teton Valley|ID065|Madison|16065|M|ee|43.8893|-111.2616
ID|065|PIH|Teton Valley|ID065|Teton|16081|M|ee|43.8893|-111.2616
ID|066|PIH|Centennial Mountains/Island Park|ID066|Clark|16033|M|ee|44.3674|-111.489
ID|066|PIH|Centennial Mountains/Island Park|ID066|Fremont|16043|M|ee|44.3674|-111.489
ID|066|PIH|Centennial Mountains/Island Park|ID066|Teton|16081|M|ee|44.3674|-111.489
ID|067|PIH|Beaverhead/Lemhi Highlands|ID067|Butte|16023|M|ee|44.2232|-112.5387
ID|067|PIH|Beaverhead/Lemhi Highlands|ID067|Clark|16033|M|ee|44.2232|-112.5387
ID|068|PIH|Lost River Valleys|ID068|Butte|16023|M|cc|43.8834|-113.4263
ID|068|PIH|Lost River Valleys|ID068|Custer|16037|M|cc|43.8834|-113.4263
ID|069|PIH|Lost River Range|ID069|Butte|16023|M|cc|44.122|-113.5633
ID|069|PIH|Lost River Range|ID069|Custer|16037|M|cc|44.122|-113.5633
ID|070|PIH|Challis/Pahsimeroi Valleys|ID070|Custer|16037|M|cc|44.4002|-114.0841
ID|071|PIH|Frank Church Wilderness|ID071|Custer|16037|M|cc|44.416|-114.5294
ID|072|PIH|Sawtooth/Stanley Basin|ID072|Blaine|16013|M|cc|44.2935|-114.9227
ID|072|PIH|Sawtooth/Stanley Basin|ID072|Custer|16037|M|cc|44.2935|-114.9227
ID|073|PIH|Sun Valley Region|ID073|Blaine|16013|M|cc|43.7253|-114.4186
ID|073|PIH|Sun Valley Region|ID073|Custer|16037|M|cc|43.7253|-114.4186
ID|074|PIH|Big Lost Highlands/Copper Basin|ID074|Blaine|16013|M|cc|43.8258|-113.9943
ID|074|PIH|Big Lost Highlands/Copper Basin|ID074|Butte|16023|M|cc|43.8258|-113.9943
ID|074|PIH|Big Lost Highlands/Copper Basin|ID074|Custer|16037|M|cc|43.8258|-113.9943
ID|075|PIH|Caribou Range|ID075|Blaine|16013|M|cc|43.4301|-114.1369
WY|001|PIH|Yellowstone National Park|WY001|Fremont|16043|M|ee|44.5976|-110.5469
AS|001|PPG|Tutuila and Aunuu|AS001|Eastern|60010|S||-14.3055|-170.717
AS|001|PPG|Tutuila and Aunuu|AS001|Western|60050|S||-14.3055|-170.717
AS|002|PPG|Manua|AS002|Manu'a|60020|S||-14.227|-169.5053
AS|003|PPG|Swains Island|AS003|Swains Island|60040|S||-11.0844|-171.046
AS|004|PPG|Rose Atoll|AS004|Rose Atoll|60030|S||-14.5453|-168.156
FM|001|PQE|Kosrae|FM001|Kosrae|64005|F||5.3102|162.9766
FM|011|PQE|Pingelap|FM011|Pingelap|64090|F||6.215|160.7044
FM|012|PQE|Mwoakilloa|FM012|Mwoakilloa|64040|F||6.68|159.7581
FM|013|PQE|Pohnpei|FM013|Pohnpei|64040|F||6.8829|158.2288
FM|014|PQE|Pakin|FM014|Pakin|64040|F||7.0649|157.8033
FM|015|PQE|Sapwuahfik|FM015|Sapwuahfik|64050|F||5.799|157.2493
FM|016|PQE|Oroluk|FM016|Oroluk|64070|F||7.5684|155.3206
FM|017|PQE|Nukuoro|FM017|Nukuoro|64060|F||3.8531|154.9572
FM|018|PQE|Kapingamarangi|FM018|Kapingamarangi|64020|F||1.0672|154.8005
MH|001|PQE|Arno|MH001|Arno|68040|K||7.0602|171.7228
MH|002|PQE|Majuro|MH002|Majuro|68190|K||7.1086|171.1789
MH|003|PQE|Wotje|MH003|Wotje|68430|K||9.4713|170.1603
MH|004|PQE|Mili|MH004|Mili|68320|K||6.0564|171.9031
MH|005|PQE|Utrok|MH005|Utrok|68410|K||11.2304|169.8404
MH|006|PQE|Jaluit|MH006|Jaluit|68120|K||5.9418|169.6133
MH|007|PQE|Ailinglaplap|MH007|Ailinglaplap|68010|J||7.3959|168.7633
MH|008|PQE|Kwajalein|MH008|Kwajalein|68150|K||9.0685|167.4829
MH|009|PQE|Ujae|MH009|Ujae|68390|K||9.1107|165.6317
MH|010|PQE|Enewetak|MH010|Enewetak|68090|K||11.4745|162.3155
FM|021|PQW|Lukunoch|FM021|Lukunoch|64420|G||5.5154|153.7735
FM|022|PQW|Losap|FM022|Losap|64410|G||6.8717|152.7215
FM|023|PQW|Chuuk Lagoon|FM023|Chuuk Lagoon|64002|G||7.3701|151.7574
FM|024|PQW|Fananu|FM024|Fananu|64350|G||8.5612|151.9124
FM|025|PQW|Onoun|FM025|Onoun|64430|G||8.5832|149.6884
FM|026|PQW|Polowat|FM026|Polowat|64610|G||7.3623|149.1871
FM|031|PQW|Satawal|FM031|Satawal|64090|G||7.3807|147.031
FM|032|PQW|Woleai|FM032|Woleai|64120|G||7.3639|143.8757
FM|033|PQW|Faraulep|FM033|Faraulep|64040|G||8.59|144.5165
FM|034|PQW|Eauripik|FM034|Eauripik|64010|G||6.6891|143.06
FM|035|PQW|Fais|FM035|Fais|64030|G||9.7631|140.5184
FM|036|PQW|Ulithi|FM036|Ulithi|64110|G||9.9895|139.7259
FM|037|PQW|Yap|FM037|Yap|64060|G||9.5399|138.127
FM|038|PQW|Ngulu|FM038|Ngulu|64080|G||8.3906|137.5069
PW|001|PQW|Kayangel|PW001|Kayangel|70100|J||8.0745|134.7146
PW|002|PQW|Melekeok|PW002|Melekeok|70212|J||7.5623|134.5852
PW|003|PQW|Airai|PW003|Airai|70004|J||7.4279|134.5428
PW|004|PQW|Koror|PW004|Koror|70150|J||7.2464|134.3979
PW|005|PQW|Peleliu|PW005|Peleliu|70350|J||7.0153|134.2477
PW|006|PQW|Angaur|PW006|Angaur|70010|J||6.9074|134.1372
PW|007|PQW|Sonsorol|PW007|Sonsorol|70370|J||5.0286|132.0991
PW|008|PQW|Tobi|PW008|Tobi|70050|J||3.0055|131.1563
AZ|530|PSR|Parker Valley|AZ530|La Paz|04012|M|sw|33.6988|-114.4568
AZ|531|PSR|Kofa|AZ531|La Paz|04012|M|sw|33.2172|-114.028
AZ|531|PSR|Kofa|AZ531|Yuma|04027|M|sw|33.2172|-114.028
AZ|532|PSR|Yuma|AZ532|Yuma|04027|M|sw|32.6544|-114.5114
AZ|533|PSR|Central La Paz|AZ533|La Paz|04012|M|sw|33.8115|-113.8132
AZ|534|PSR|Aguila Valley|AZ534|Maricopa|04013|M|sc|33.8662|-112.9785
AZ|535|PSR|Southeast Yuma County|AZ535|Yuma|04027|M|sw|32.3859|-113.7573
AZ|536|PSR|Gila River Valley|AZ536|Yuma|04027|M|sw|32.822|-113.804
AZ|537|PSR|Northwest Valley|AZ537|Maricopa|04013|M|sc|33.7421|-112.477
AZ|538|PSR|Tonopah Desert|AZ538|Maricopa|04013|M|sc|33.3971|-112.9704
AZ|539|PSR|Gila Bend|AZ539|Maricopa|04013|M|sc|32.8542|-113.0566
AZ|540|PSR|Buckeye/Avondale|AZ540|Maricopa|04013|M|sc|33.3912|-112.4004
AZ|541|PSR|Cave Creek/New River|AZ541|Maricopa|04013|M|sc|33.8086|-112.0129
AZ|542|PSR|Deer Valley|AZ542|Maricopa|04013|M|sc|33.7122|-112.1301
AZ|543|PSR|Central Phoenix|AZ543|Maricopa|04013|M|sc|33.4331|-112.0552
AZ|544|PSR|North Phoenix/Glendale|AZ544|Maricopa|04013|M|sc|33.5716|-112.1525
AZ|545|PSR|New River Mesa|AZ545|Maricopa|04013|M|sc|33.926|-111.8887
AZ|546|PSR|Scottsdale/Paradise Valley|AZ546|Maricopa|04013|M|sc|33.5351|-111.8891
AZ|547|PSR|Rio Verde/Salt River|AZ547|Maricopa|04013|M|sc|33.7012|-111.51
AZ|548|PSR|East Valley|AZ548|Maricopa|04013|M|sc|33.3765|-111.8134
AZ|549|PSR|Fountain Hills/East Mesa|AZ549|Maricopa|04013|M|sc|33.5349|-111.6592
AZ|550|PSR|South Mountain/Ahwatukee|AZ550|Maricopa|04013|M|sc|33.2829|-112.0449
AZ|551|PSR|Southeast Valley/Queen Creek|AZ551|Maricopa|04013|M|sc|33.2616|-111.7353
AZ|552|PSR|Superior|AZ552|Pinal|04021|M|sc|33.2702|-111.188
AZ|553|PSR|Northwest Pinal County|AZ553|Pinal|04021|M|sc|33.0208|-111.7511
AZ|554|PSR|West Pinal County|AZ554|Pinal|04021|P|sc|32.8658|-112.1203
AZ|555|PSR|Apache Junction/Gold Canyon|AZ555|Pinal|04021|M|sc|33.2584|-111.3827
AZ|556|PSR|Tonto Basin|AZ556|Gila|04007|M|sc|33.7079|-111.1275
AZ|557|PSR|Mazatzal Mountains|AZ557|Gila|04007|M|sc|33.8233|-111.4206
AZ|557|PSR|Mazatzal Mountains|AZ557|Maricopa|04013|M|sc|33.8233|-111.4206
AZ|558|PSR|Pinal/Superstition Mountains|AZ558|Gila|04007|M|sc|33.3639|-110.9698
AZ|558|PSR|Pinal/Superstition Mountains|AZ558|Maricopa|04013|M|sc|33.3639|-110.9698
AZ|558|PSR|Pinal/Superstition Mountains|AZ558|Pinal|04021|M|sc|33.3639|-110.9698
AZ|559|PSR|Sonoran Desert Natl Monument|AZ559|Maricopa|04013|M|sc|32.8019|-112.5236
AZ|560|PSR|San Carlos|AZ560|Gila|04007|M|sc|33.3416|-110.5321
AZ|561|PSR|Dripping Springs|AZ561|Gila|04007|M|sc|33.102|-110.7854
AZ|562|PSR|Globe/Miami|AZ562|Gila|04007|M|sc|33.4344|-110.8175
AZ|563|PSR|Southeast Gila County|AZ563|Gila|04007|M|sc|33.6107|-110.4548
CA|560|PSR|Joshua Tree NP West|CA560|San Bernardino|06071|P|ss|33.9359|-116.0847
CA|561|PSR|Joshua Tree NP East|CA561|San Bernardino|06071|P|ss|33.9564|-115.6533
CA|562|PSR|Imperial County Southwest|CA562|Imperial|06025|P|se|32.8129|-116.039
CA|563|PSR|Salton Sea|CA563|Imperial|06025|P|se|33.3091|-115.8096
CA|563|PSR|Salton Sea|CA563|Riverside|06065|P|se|33.3091|-115.8096
CA|564|PSR|Chuckwalla Mountains|CA564|Imperial|06025|P|se|33.3715|-115.2724
CA|564|PSR|Chuckwalla Mountains|CA564|Riverside|06065|P|se|33.3715|-115.2724
CA|565|PSR|Imperial County Southeast|CA565|Imperial|06025|P|se|32.886|-114.9902
CA|566|PSR|Imperial County West|CA566|Imperial|06025|P|se|32.9908|-115.9008
CA|567|PSR|Imperial Valley|CA567|Imperial|06025|P|se|32.9245|-115.5185
CA|568|PSR|Chiriaco Summit|CA568|Riverside|06065|P|ss|33.6785|-115.6832
CA|569|PSR|Palo Verde Valley|CA569|Imperial|06025|P|se|33.4256|-114.6527
CA|569|PSR|Palo Verde Valley|CA569|Riverside|06065|P|se|33.4256|-114.6527
CA|570|PSR|Chuckwalla Valley|CA570|Riverside|06065|P|se|33.8125|-115.0182
CO|058|PUB|Western Mosquito Range/East Lake County Above 11000 Ft|CO058|Lake|08065|M|cc|39.2545|-106.2141
CO|059|PUB|Leadville Vicinity/Lake County Below 11000 Ft|CO059|Lake|08065|M|cc|39.1873|-106.3446
CO|060|PUB|Eastern Sawatch Mountains above 11000 Ft|CO060|Chaffee|08015|M|cc|38.8197|-106.3586
CO|060|PUB|Eastern Sawatch Mountains above 11000 Ft|CO060|Lake|08065|M|cc|38.8197|-106.3586
CO|060|PUB|Eastern Sawatch Mountains above 11000 Ft|CO060|Saguache|08109|M|cc|38.8197|-106.3586
CO|061|PUB|Western Chaffee County Between 9000 and 11000 Ft|CO061|Chaffee|08015|M|cc|38.7415|-106.2559
CO|062|PUB|Central Chaffee County Below 9000 Ft|CO062|Chaffee|08015|M|cc|38.6873|-106.0928
CO|063|PUB|Western Mosquito Range/East Chaffee County above 9000Ft|CO063|Chaffee|08015|M|cc|38.8243|-106.0253
CO|064|PUB|Saguache County West of Continental Divide Below 10000 Ft|CO064|Saguache|08109|M|cc|38.3063|-106.7044
CO|065|PUB|Saguache County East of Continental Divide below 10000 Ft|CO065|Rio Grande|08105|M|sc|38.1071|-106.3423
CO|065|PUB|Saquache County East of Continental Divide below 10000 Ft|CO065|Saguache|08109|M|cc|38.1071|-106.3423
CO|066|PUB|La Garita Mountains Above 10000 Ft|CO066|Mineral|08079|M|sc|38.0229|-106.7318
CO|066|PUB|La Garita Mountains Above 10000 Ft|CO066|Rio Grande|08105|M|sc|38.0229|-106.7318
CO|066|PUB|La Garita Mountains Above 10000 Ft|CO066|Saguache|08109|M|cc|38.0229|-106.7318
CO|067|PUB|Upper Rio Grande Valley/Eastern San Juan Mountains Below 10000 Ft|CO067|Conejos|08021|M|sc|37.469|-106.5413
CO|067|PUB|Upper Rio Grande Valley/Eastern San Juan Mountains Below 10000 Ft|CO067|Mineral|08079|M|sc|37.469|-106.5413
CO|067|PUB|Upper Rio Grande Valley/Eastern San Juan Mountains Below 10000 Ft|CO067|Rio Grande|08105|M|sc|37.469|-106.5413
CO|068|PUB|Eastern San Juan Mountains Above 10000 Ft|CO068|Conejos|08021|M|sc|37.4272|-106.7002
CO|068|PUB|Eastern San Juan Mountains Above 10000 Ft|CO068|Mineral|08079|M|sc|37.4272|-106.7002
CO|068|PUB|Eastern San Juan Mountains Above 10000 Ft|CO068|Rio Grande|08105|M|sc|37.4272|-106.7002
CO|069|PUB|Del Norte Vicinity/Northern San Luis Valley Below 8500 Ft|CO069|Rio Grande|08105|M|sc|37.9152|-106.0347
CO|069|PUB|Del Norte Vicinity/Northern San Luis Valley Below 8500 Ft|CO069|Saguache|08109|M|cc|37.9152|-106.0347
CO|070|PUB|Alamosa  Vicinity/Central San Luis Valley Below 8500 Ft|CO070|Alamosa|08003|M|sc|37.5614|-105.8929
CO|070|PUB|Alamosa  Vicinity/Central San Luis Valley Below 8500 Ft|CO070|Rio Grande|08105|M|sc|37.5614|-105.8929
CO|071|PUB|Southern San Luis Valley|CO071|Conejos|08021|M|sc|37.2224|-105.7537
CO|071|PUB|Southern San Luis Valley|CO071|Costilla|08023|M|sc|37.2224|-105.7537
CO|072|PUB|Northern Sangre de Cristo Mountains Between 8500 And 11000 Ft|CO072|Alamosa|08003|M|sc|37.9018|-105.5379
CO|072|PUB|Northern Sangre de Cristo Mountains Between 8500 And 11000 Ft|CO072|Chaffee|08015|M|cc|37.9018|-105.5379
CO|072|PUB|Northern Sangre de Cristo Mountains Between 8500 And 11000 Ft|CO072|Costilla|08023|M|sc|37.9018|-105.5379
CO|072|PUB|Northern Sangre de Cristo Mountains Between 8500 And 11000 Ft|CO072|Custer|08027|M|se|37.9018|-105.5379
CO|072|PUB|Northern Sangre de Cristo Mountains Between 8500 And 11000 Ft|CO072|Fremont|08043|M|cc|37.9018|-105.5379
CO|072|PUB|Northern Sangre de Christo Mountains Between 8500 And 11000 Ft|CO072|Huerfano|08055|M|se|37.9018|-105.5379
CO|072|PUB|Northern Sangre de Cristo Mountains Between 8500 And 11000 Ft|CO072|Saguache|08109|M|cc|37.9018|-105.5379
CO|073|PUB|Northern Sangre de Cristo Mountains above 11000 Ft|CO073|Alamosa|08003|M|sc|37.9767|-105.617
CO|073|PUB|Northern Sangre de Cristo Mountains above 11000 Ft|CO073|Costilla|08023|M|sc|37.9767|-105.617
CO|073|PUB|Northern Sangre de Cristo Mountains above 11000 Ft|CO073|Custer|08027|M|se|37.9767|-105.617
CO|073|PUB|Northern Sangre de Cristo Mountains above 11000 Ft|CO073|Fremont|08043|M|cc|37.9767|-105.617
CO|073|PUB|Northern Sangre de Cristo Mountains above 11000 Ft|CO073|Huerfano|08055|M|se|37.9767|-105.617
CO|073|PUB|Northern Sangre de Cristo Mountains above 11000 Ft|CO073|Saguache|08109|M|cc|37.9767|-105.617
CO|074|PUB|Southern Sangre De Cristo Mountains Between 7500 and 11000 Ft|CO074|Costilla|08023|M|sc|37.2245|-105.0257
CO|074|PUB|Southern Sangre De Cristo Mountains Between 7500 and 11000 Ft|CO074|Huerfano|08055|M|se|37.2245|-105.0257
CO|074|PUB|Southern Sangre De Cristo Mountains Between 7500 and 11000 Ft|CO074|Las Animas|08071|M|se|37.2245|-105.0257
CO|075|PUB|Southern Sangre De Cristo Mountains Above 11000 Ft|CO075|Costilla|08023|M|sc|37.2046|-105.1708
CO|075|PUB|Southern Sangre De Cristo Mountains Above 11000 Ft|CO075|Huerfano|08055|M|se|37.2046|-105.1708
CO|075|PUB|Southern Sangre De Cristo Mountains Above 11000 Ft|CO075|Las Animas|08071|M|se|37.2046|-105.1708
CO|076|PUB|Northwestern Fremont County  Above 8500Ft|CO076|Fremont|08043|M|cc|38.6011|-105.6475
CO|077|PUB|Western/Central Fremont County Below 8500 Ft|CO077|Fremont|08043|M|cc|38.4248|-105.5558
CO|078|PUB|Wet Mountain Valley Below 8500 Ft|CO078|Custer|08027|M|se|38.1353|-105.4502
CO|078|PUB|Wet Mountain Valley Below 8500 Ft|CO078|Huerfano|08055|M|se|38.1353|-105.4502
CO|079|PUB|Wet Mountains between 6300 and 10000Ft|CO079|Custer|08027|M|se|38.046|-105.1469
CO|079|PUB|Wet Mountains between 6300 and 10000Ft|CO079|Fremont|08043|M|cc|38.046|-105.1469
CO|079|PUB|Wet Mountains between 6300 and 10000Ft|CO079|Huerfano|08055|M|se|38.046|-105.1469
CO|079|PUB|Wet Mountains between 6300 and 10000Ft|CO079|Pueblo|08101|M|se|38.046|-105.1469
CO|080|PUB|Wet Mountains above 10000 Ft|CO080|Custer|08027|M|se|37.9888|-105.1345
CO|080|PUB|Wet Mountains above 10000 Ft|CO080|Huerfano|08055|M|se|37.9888|-105.1345
CO|080|PUB|Wet Mountains above 10000 Ft|CO080|Pueblo|08101|M|se|37.9888|-105.1345
CO|081|PUB|Teller County/Rampart Range above 7500fT/Pike's Peak Between 7500 And 11000 Ft|CO081|El Paso|08041|M|ec|38.8708|-105.113
CO|081|PUB|Teller County/Rampart Range above 7500fT/Pike's Peak Between 7500 And 11000 Ft|CO081|Fremont|08043|M|cc|38.8708|-105.113
CO|081|PUB|Teller County/Rampart Range above 7500fT/Pike's Peak Between 7500 And 11000 Ft|CO081|Teller|08119|M|cc|38.8708|-105.113
CO|082|PUB|Pikes Peak above 11000 Ft|CO082|El Paso|08041|M|ec|38.8156|-105.0464
CO|082|PUB|Pikes Peak above 11000 Ft|CO082|Teller|08119|M|cc|38.8156|-105.0464
CO|083|PUB|Canon City Vicinity/Eastern Fremont County|CO083|Custer|08027|M|se|38.4443|-105.1148
CO|083|PUB|Canon City Vicinity/Eastern Fremont County|CO083|Fremont|08043|M|cc|38.4443|-105.1148
CO|083|PUB|Canon City Vicinity/Eastern Fremont County|CO083|Teller|08119|M|cc|38.4443|-105.1148
CO|084|PUB|Northern El Paso County/Monument Ridge/Rampart Range Below 7500 Ft|CO084|El Paso|08041|M|ec|39.0124|-104.4498
CO|085|PUB|Colorado Springs Vicinity/Southern El Paso County/Rampart Range Below 7400 Ft|CO085|El Paso|08041|M|ec|38.7125|-104.5034
CO|086|PUB|Pueblo Vicinity/Pueblo County Below 6300 Feet|CO086|Pueblo|08101|M|se|38.1821|-104.4872
CO|087|PUB|Walsenburg Vicinity/Upper Huerfano River Basin Below 7500 Ft|CO087|Huerfano|08055|M|se|37.6899|-104.8578
CO|088|PUB|Trinidad Vicinity/Western Las Animas County Below 7500 Ft|CO088|Las Animas|08071|M|se|37.3538|-104.3935
CO|089|PUB|Crowley County|CO089|Crowley|08025|M|se|38.3266|-103.7849
CO|093|PUB|La Junta Vicinity/Otero County|CO093|Otero|08089|M|se|37.9027|-103.7164
CO|094|PUB|Eastern Las Animas County|CO094|Las Animas|08071|M|se|37.3221|-103.5645
CO|095|PUB|Western Kiowa County|CO095|Kiowa|08061|M|se|38.424|-103.0919
CO|096|PUB|Eastern Kiowa County|CO096|Kiowa|08061|M|se|38.4414|-102.3891
CO|097|PUB|Las Animas Vicinity/Bent County|CO097|Bent|08011|M|se|37.9551|-103.0717
CO|098|PUB|Lamar Vicinity/Prowers County|CO098|Prowers|08099|M|se|37.9552|-102.3933
CO|099|PUB|Springfield Vicinity/Baca County|CO099|Baca|08009|M|se|37.3192|-102.5605
NC|007|RAH|Person|NC007|Person|37145|E|cc|36.3901|-78.9717
NC|008|RAH|Granville|NC008|Granville|37077|E|cc|36.304|-78.653
NC|009|RAH|Vance|NC009|Vance|37181|E|cc|36.3648|-78.4083
NC|010|RAH|Warren|NC010|Warren|37185|E|cc|36.3966|-78.1069
NC|011|RAH|Halifax|NC011|Halifax|37083|E|cc|36.2575|-77.6519
NC|021|RAH|Forsyth|NC021|Forsyth|37067|E|cc|36.1304|-80.2563
NC|022|RAH|Guilford|NC022|Guilford|37081|E|cc|36.0794|-79.789
NC|023|RAH|Alamance|NC023|Alamance|37001|E|cc|36.044|-79.3995
NC|024|RAH|Orange|NC024|Orange|37135|E|cc|36.0614|-79.1205
NC|025|RAH|Durham|NC025|Durham|37063|E|cc|36.0359|-78.8764
NC|026|RAH|Franklin|NC026|Franklin|37069|E|cc|36.0827|-78.2857
NC|027|RAH|Nash|NC027|Nash|37127|E|cc|35.9672|-77.9865
NC|028|RAH|Edgecombe|NC028|Edgecombe|37065|E|cc|35.9129|-77.5971
NC|038|RAH|Davidson|NC038|Davidson|37057|E|cc|35.7932|-80.2127
NC|039|RAH|Randolph|NC039|Randolph|37151|E|cc|35.7103|-79.806
NC|040|RAH|Chatham|NC040|Chatham|37037|E|cc|35.7028|-79.2553
NC|041|RAH|Wake|NC041|Wake|37183|E|cc|35.7901|-78.6504
NC|042|RAH|Johnston|NC042|Johnston|37101|E|cc|35.5176|-78.3657
NC|043|RAH|Wilson|NC043|Wilson|37195|E|cc|35.7048|-77.9185
NC|073|RAH|Stanly|NC073|Stanly|37167|E|cc|35.312|-80.2507
NC|074|RAH|Montgomery|NC074|Montgomery|37123|E|cc|35.3324|-79.9054
NC|075|RAH|Moore|NC075|Moore|37125|E|cc|35.3107|-79.4813
NC|076|RAH|Lee|NC076|Lee|37105|E|cc|35.475|-79.1716
NC|077|RAH|Harnett|NC077|Harnett|37085|E|cc|35.3687|-78.8693
NC|078|RAH|Wayne|NC078|Wayne|37191|E|cc|35.3638|-78.004
NC|083|RAH|Anson|NC083|Anson|37007|E|cc|34.9738|-80.1027
NC|084|RAH|Richmond|NC084|Richmond|37153|E|cc|35.0059|-79.748
NC|085|RAH|Scotland|NC085|Scotland|37165|E|cc|34.8411|-79.4805
NC|086|RAH|Hoke|NC086|Hoke|37093|E|cc|35.0174|-79.2371
NC|088|RAH|Cumberland|NC088|Cumberland|37051|E|cc|35.0485|-78.8273
NC|089|RAH|Sampson|NC089|Sampson|37163|E|cc|34.9915|-78.3712
CA|070|REV|Surprise Valley California|CA070|Modoc|06049|P|nn|41.6116|-120.0862
CA|071|REV|Lassen-Eastern Plumas-Eastern Sierra Counties|CA071|Lassen|06035|P|nn|40.466|-120.5471
CA|071|REV|Lassen-Eastern Plumas-Eastern Sierra Counties|CA071|Plumas|06063|P|nn|40.466|-120.5471
CA|071|REV|Lassen-Eastern Plumas-Eastern Sierra Counties|CA071|Sierra|06091|P|nn|40.466|-120.5471
CA|072|REV|Greater Lake Tahoe Area|CA072|Alpine|06003|P|cc|38.9481|-119.9683
CA|072|REV|Greater Lake Tahoe Area|CA072|El Dorado|06017|P|cc|38.9481|-119.9683
CA|072|REV|Greater Lake Tahoe Area|CA072|Nevada|06057|P|cc|38.9481|-119.9683
CA|072|REV|Greater Lake Tahoe Area|CA072|Placer|06061|P|cc|38.9481|-119.9683
CA|073|REV|Mono|CA073|Mono|06051|P|cc|37.939|-118.8867
NV|001|REV|Mineral and Southern Lyon Counties|NV001|Lyon|32019|P|ww|38.6067|-118.6034
NV|001|REV|Mineral and Southern Lyon Counties|NV001|Mineral|32021|P|ww|38.6067|-118.6034
NV|002|REV|Greater Lake Tahoe Area|NV002|Douglas|32005|P|ww|39.2153|-119.9149
NV|002|REV|Greater Lake Tahoe Area|NV002|Washoe|32031|P|ww|39.2153|-119.9149
NV|002|REV|Greater Lake Tahoe Area|NV002|Carson City|32510|P|ww|39.2153|-119.9149
NV|003|REV|Greater Reno-Carson City-Minden Area|NV003|Douglas|32005|P|ww|39.4151|-119.6557
NV|003|REV|Greater Reno-Carson City-Minden Area|NV003|Lyon|32019|P|ww|39.4151|-119.6557
NV|003|REV|Greater Reno-Carson City-Minden Area|NV003|Storey|32029|P|ww|39.4151|-119.6557
NV|003|REV|Greater Reno-Carson City-Minden Area|NV003|Washoe|32031|P|ww|39.4151|-119.6557
NV|003|REV|Greater Reno-Carson City-Minden Area|NV003|Carson City|32510|P|ww|39.4151|-119.6557
NV|004|REV|Western Nevada Basin and Range including Pyramid Lake|NV004|Churchill|32001|P|wc|40.0152|-118.49
NV|004|REV|Western Nevada Basin and Range including Pyramid Lake|NV004|Lyon|32019|P|ww|40.0152|-118.49
NV|004|REV|Western Nevada Basin and Range including Pyramid Lake|NV004|Pershing|32027|P|wc|40.0152|-118.49
NV|004|REV|Western Nevada Basin and Range including Pyramid Lake|NV004|Washoe|32031|P|ww|40.0152|-118.49
NV|005|REV|Northern Washoe County|NV005|Washoe|32031|P|ww|41.1126|-119.6686
WY|001|RIW|Yellowstone National Park|WY001|Park|56029|M|nw|44.5976|-110.5469
WY|001|RIW|Yellowstone National Park|WY001|Teton|56039|M|nw|44.5976|-110.5469
WY|002|RIW|Absaroka Mountains|WY002|Fremont|56013|M|cc|44.2172|-109.5521
WY|002|RIW|Absaroka Mountains|WY002|Hot Springs|56017|M|cc|44.2172|-109.5521
WY|002|RIW|Absaroka Mountains|WY002|Park|56029|M|nw|44.2172|-109.5521
WY|003|RIW|Cody Foothills|WY003|Park|56029|M|nw|44.4594|-109.0463
WY|004|RIW|North Big Horn Basin|WY004|Big Horn|56003|M|nc|44.5447|-108.3008
WY|004|RIW|North Big Horn Basin|WY004|Park|56029|M|nw|44.5447|-108.3008
WY|005|RIW|Southwest Big Horn Basin|WY005|Hot Springs|56017|M|cc|43.7774|-108.2779
WY|006|RIW|Southeast Big Horn Basin|WY006|Washakie|56043|M|nc|43.9423|-107.8197
WY|007|RIW|Owl Creek and Bridger Mountains|WY007|Fremont|56013|M|cc|43.573|-108.2336
WY|007|RIW|Owl Creek and Bridger Mountains|WY007|Hot Springs|56017|M|cc|43.573|-108.2336
WY|007|RIW|Owl Creek and Bridger Mountains|WY007|Natrona|56025|M|cc|43.573|-108.2336
WY|008|RIW|Bighorn Mountains West|WY008|Big Horn|56003|M|nc|44.2518|-107.4682
WY|008|RIW|Bighorn Mountains West|WY008|Fremont|56013|M|cc|44.2518|-107.4682
WY|008|RIW|Bighorn Mountains West|WY008|Johnson|56019|M|nc|44.2518|-107.4682
WY|008|RIW|Bighorn Mountains West|WY008|Natrona|56025|M|cc|44.2518|-107.4682
WY|008|RIW|Bighorn Mountains West|WY008|Washakie|56043|M|nc|44.2518|-107.4682
WY|009|RIW|Bighorn Mountains Southeast|WY009|Johnson|56019|M|nc|43.9099|-107.0263
WY|009|RIW|Bighorn Mountains Southeast|WY009|Natrona|56025|M|cc|43.9099|-107.0263
WY|009|RIW|Bighorn Mountains Southeast|WY009|Washakie|56043|M|nc|43.9099|-107.0263
WY|010|RIW|Northeast Johnson County|WY010|Johnson|56019|M|nc|44.368|-106.4299
WY|011|RIW|Southeast Johnson County|WY011|Johnson|56019|M|nc|43.8206|-106.4368
WY|012|RIW|Teton and Gros Ventre Mountains|WY012|Fremont|56013|M|cc|43.6883|-110.5055
WY|012|RIW|Teton and Gros Ventre Mountains|WY012|Lincoln|56023|M|wc|43.6883|-110.5055
WY|012|RIW|Teton and Gros Ventre Mountains|WY012|Sublette|56035|M|wc|43.6883|-110.5055
WY|012|RIW|Teton and Gros Ventre Mountains|WY012|Teton|56039|M|nw|43.6883|-110.5055
WY|013|RIW|Jackson Hole|WY013|Lincoln|56023|M|wc|43.6458|-110.6864
WY|013|RIW|Jackson Hole|WY013|Teton|56039|M|nw|43.6458|-110.6864
WY|014|RIW|Wind River Mountains West|WY014|Fremont|56013|M|cc|42.9092|-109.4923
WY|014|RIW|Wind River Mountains West|WY014|Sublette|56035|M|wc|42.9092|-109.4923
WY|015|RIW|Wind River Mountains East|WY015|Fremont|56013|M|cc|43.0496|-109.2855
WY|015|RIW|Wind River Mountains East|WY015|Sublette|56035|M|wc|43.0496|-109.2855
WY|016|RIW|Upper Wind River Basin|WY016|Fremont|56013|M|cc|43.4505|-109.339
WY|017|RIW|Wind River Basin|WY017|Fremont|56013|M|cc|43.1357|-108.2754
WY|018|RIW|Lander Foothills|WY018|Fremont|56013|M|cc|42.797|-108.6388
WY|019|RIW|Green Mountains and Rattlesnake Range|WY019|Fremont|56013|M|cc|42.4379|-107.9137
WY|019|RIW|Green Mountains and Rattlesnake Range|WY019|Natrona|56025|M|cc|42.4379|-107.9137
WY|019|RIW|Green Mountains and Rattlesnake Range|WY019|Sweetwater|56037|M|sc|42.4379|-107.9137
WY|020|RIW|Natrona County Lower Elevations|WY020|Natrona|56025|M|cc|43.066|-106.6783
WY|022|RIW|Casper Mountain|WY022|Natrona|56025|M|cc|42.6061|-106.2637
WY|023|RIW|Star Valley|WY023|Lincoln|56023|M|wc|42.8634|-110.982
WY|024|RIW|Salt River and Wyoming Ranges|WY024|Lincoln|56023|M|wc|42.5626|-110.6654
WY|024|RIW|Salt River and Wyoming Ranges|WY024|Sublette|56035|M|wc|42.5626|-110.6654
WY|025|RIW|Upper Green River Basin Foothills|WY025|Sublette|56035|M|wc|42.9803|-110.0392
WY|026|RIW|Upper Green River Basin|WY026|Fremont|56013|M|cc|42.3437|-109.7743
WY|026|RIW|Upper Green River Basin|WY026|Lincoln|56023|M|wc|42.3437|-109.7743
WY|026|RIW|Upper Green River Basin|WY026|Sublette|56035|M|wc|42.3437|-109.7743
WY|026|RIW|Upper Green River Basin|WY026|Sweetwater|56037|M|sc|42.3437|-109.7743
WY|027|RIW|South Lincoln County|WY027|Lincoln|56023|M|wc|41.8212|-110.5572
WY|028|RIW|Rock Springs and Green River|WY028|Sweetwater|56037|M|sc|41.5579|-109.6723
WY|029|RIW|Flaming Gorge|WY029|Sweetwater|56037|M|sc|41.2424|-109.4375
WY|030|RIW|East Sweetwater County|WY030|Sweetwater|56037|M|sc|41.5802|-108.4192
KY|101|RLX|Greenup|KY101|Greenup|21089|E||38.5456|-82.9223
KY|102|RLX|Carter|KY102|Carter|21043|E||38.3181|-83.0495
KY|103|RLX|Boyd|KY103|Boyd|21019|E||38.3596|-82.6877
KY|105|RLX|Lawrence|KY105|Lawrence|21127|E||38.0679|-82.7347
OH|066|RLX|Perry|OH066|Perry|39127|E|se|39.7371|-82.2361
OH|067|RLX|Morgan|OH067|Morgan|39115|E|se|39.6203|-81.8527
OH|075|RLX|Athens|OH075|Athens|39009|E|se|39.3337|-82.0452
OH|076|RLX|Washington|OH076|Washington|39167|E|se|39.4553|-81.4953
OH|083|RLX|Jackson|OH083|Jackson|39079|E|se|39.0197|-82.6184
OH|084|RLX|Vinton|OH084|Vinton|39163|E|se|39.251|-82.4854
OH|085|RLX|Meigs|OH085|Meigs|39105|E|se|39.0821|-82.0229
OH|086|RLX|Gallia|OH086|Gallia|39053|E|se|38.8248|-82.3169
OH|087|RLX|Lawrence|OH087|Lawrence|39087|E|se|38.5985|-82.5368
VA|003|RLX|Dickenson|VA003|Dickenson|51051|E||37.1258|-82.3503
VA|004|RLX|Buchanan|VA004|Buchanan|51027|E||37.2666|-82.036
WV|005|RLX|Wayne|WV005|Wayne|54099|E||38.1461|-82.427
WV|006|RLX|Cabell|WV006|Cabell|54011|E||38.4203|-82.2417
WV|007|RLX|Mason|WV007|Mason|54053|E||38.7698|-82.0265
WV|008|RLX|Jackson|WV008|Jackson|54035|E||38.8344|-81.6748
WV|009|RLX|Wood|WV009|Wood|54107|E||39.2111|-81.515
WV|010|RLX|Pleasants|WV010|Pleasants|54073|E||39.3709|-81.1606
WV|011|RLX|Tyler|WV011|Tyler|54095|E||39.4653|-80.8849
WV|013|RLX|Lincoln|WV013|Lincoln|54043|E||38.1753|-82.0705
WV|014|RLX|Putnam|WV014|Putnam|54079|E||38.5086|-81.909
WV|015|RLX|Kanawha|WV015|Kanawha|54039|E||38.3365|-81.5281
WV|016|RLX|Roane|WV016|Roane|54087|E||38.714|-81.3483
WV|017|RLX|Wirt|WV017|Wirt|54105|E||39.0224|-81.3786
WV|018|RLX|Calhoun|WV018|Calhoun|54013|E||38.8445|-81.1175
WV|019|RLX|Ritchie|WV019|Ritchie|54085|E||39.1783|-81.0629
WV|020|RLX|Doddridge|WV020|Doddridge|54017|E||39.2692|-80.707
WV|024|RLX|Mingo|WV024|Mingo|54059|E||37.7264|-82.1346
WV|025|RLX|Logan|WV025|Logan|54045|E||37.8316|-81.9353
WV|026|RLX|Boone|WV026|Boone|54005|E||38.0231|-81.7113
WV|027|RLX|Clay|WV027|Clay|54015|E||38.4626|-81.075
WV|028|RLX|Braxton|WV028|Braxton|54007|E||38.6998|-80.7193
WV|029|RLX|Gilmer|WV029|Gilmer|54021|E||38.9241|-80.8571
WV|030|RLX|Lewis|WV030|Lewis|54041|E||38.9958|-80.5022
WV|031|RLX|Harrison|WV031|Harrison|54033|E||39.2835|-80.3798
WV|032|RLX|Taylor|WV032|Taylor|54091|E||39.336|-80.0461
WV|033|RLX|McDowell|WV033|McDowell|54047|E||37.3785|-81.6536
WV|034|RLX|Wyoming|WV034|Wyoming|54109|E||37.6096|-81.5491
WV|039|RLX|Upshur|WV039|Upshur|54097|E||38.8978|-80.2334
WV|040|RLX|Barbour|WV040|Barbour|54001|E||39.1329|-80.003
WV|515|RLX|Northwest Raleigh|WV515|Raleigh|54081|E|se|37.8161|-81.3664
WV|516|RLX|Southeast Raleigh|WV516|Raleigh|54081|E|se|37.7176|-81.1069
WV|517|RLX|Northwest Fayette|WV517|Fayette|54019|E|se|38.0705|-81.1522
WV|518|RLX|Southeast Fayette|WV518|Fayette|54019|E|se|37.9361|-80.9236
WV|519|RLX|Northwest Nicholas|WV519|Nicholas|54067|E|se|38.3224|-80.8474
WV|520|RLX|Southeast Nicholas|WV520|Nicholas|54067|E|se|38.1937|-80.6455
WV|521|RLX|Northwest Webster|WV521|Webster|54101|E|ne|38.5398|-80.4692
WV|522|RLX|Southeast Webster|WV522|Webster|54101|E|ne|38.4185|-80.3419
WV|523|RLX|Northwest Pocahontas|WV523|Pocahontas|54075|E|ne|38.429|-79.9797
WV|524|RLX|Southeast Pocahontas|WV524|Pocahontas|54075|E|ne|38.2241|-80.0388
WV|525|RLX|Northwest Randolph|WV525|Randolph|54083|E|ne|38.8495|-79.9622
WV|526|RLX|Southeast Randolph|WV526|Randolph|54083|E|ne|38.7298|-79.8239
NC|001|RNK|Ashe|NC001|Ashe|37009|E|nw|36.4346|-81.501
NC|002|RNK|Alleghany|NC002|Alleghany|37005|E|nw|36.4915|-81.1286
NC|003|RNK|Surry|NC003|Surry|37171|E|nc|36.4148|-80.6882
NC|004|RNK|Stokes|NC004|Stokes|37169|E|nc|36.4018|-80.2395
NC|005|RNK|Rockingham|NC005|Rockingham|37157|E|nc|36.3961|-79.7751
NC|006|RNK|Caswell|NC006|Caswell|37033|E|nc|36.3934|-79.3337
NC|018|RNK|Watauga|NC018|Watauga|37189|E|nw|36.2313|-81.6969
NC|019|RNK|Wilkes|NC019|Wilkes|37193|E|nw|36.2065|-81.1638
NC|020|RNK|Yadkin|NC020|Yadkin|37197|E|nw|36.1605|-80.6653
VA|007|RNK|Tazewell|VA007|Tazewell|51185|E|sw|37.125|-81.5606
VA|009|RNK|Smyth|VA009|Smyth|51173|E|sw|36.8439|-81.537
VA|010|RNK|Bland|VA010|Bland|51021|E|sw|37.134|-81.1302
VA|011|RNK|Giles|VA011|Giles|51071|E|sw|37.3141|-80.7037
VA|012|RNK|Wythe|VA012|Wythe|51197|E|sw|36.9171|-81.0786
VA|013|RNK|Pulaski|VA013|Pulaski|51155|E|sw|37.0654|-80.7096
VA|013|RNK|Pulaski|VA013|City of Radford|51750|E|sw|37.0654|-80.7096
VA|014|RNK|Montgomery|VA014|Montgomery|51121|E|sw|37.174|-80.3869
VA|015|RNK|Grayson|VA015|Grayson|51077|E|sw|36.6566|-81.225
VA|016|RNK|Carroll|VA016|Carroll|51035|E|sw|36.7304|-80.737
VA|016|RNK|Carroll|VA016|City of Galax|51640|E|sw|36.7304|-80.737
VA|017|RNK|Floyd|VA017|Floyd|51063|E|sw|36.9315|-80.3626
VA|018|RNK|Craig|VA018|Craig|51045|E|sw|37.4813|-80.2123
VA|019|RNK|Alleghany|VA019|Alleghany|51005|E|wc|37.7875|-80.0067
VA|019|RNK|Alleghany|VA019|City of Covington|51580|E|wc|37.7875|-80.0067
VA|020|RNK|Bath|VA020|Bath|51017|E|wc|38.0587|-79.7411
VA|022|RNK|Roanoke|VA022|Roanoke|51161|E|wc|37.2714|-80.052
VA|022|RNK|Roanoke|VA022|City of Roanoke|51770|E|wc|37.2714|-80.052
VA|022|RNK|Roanoke|VA022|City of Salem|51775|E|wc|37.2714|-80.052
VA|023|RNK|Botetourt|VA023|Botetourt|51023|E|wc|37.5571|-79.8123
VA|024|RNK|Rockbridge|VA024|Rockbridge|51163|E|wc|37.8136|-79.4465
VA|024|RNK|Rockbridge|VA024|City of Buena Vista|51530|E|wc|37.8136|-79.4465
VA|024|RNK|Rockbridge|VA024|City of Lexington|51678|E|wc|37.8136|-79.4465
VA|032|RNK|Patrick|VA032|Patrick|51141|E|sw|36.6784|-80.2843
VA|033|RNK|Franklin|VA033|Franklin|51067|E|wc|36.992|-79.881
VA|034|RNK|Bedford|VA034|Bedford|51019|E|sc|37.3152|-79.5242
VA|035|RNK|Amherst|VA035|Amherst|51009|E|cc|37.6048|-79.1451
VA|043|RNK|Henry|VA043|Henry|51089|E|sc|36.6828|-79.8736
VA|043|RNK|Henry|VA043|City of Martinsville|51690|E|sc|36.6828|-79.8736
VA|044|RNK|Pittsylvania|VA044|Pittsylvania|51143|E|sc|36.8111|-79.3976
VA|044|RNK|Pittsylvania|VA044|City of Danville|51590|E|sc|36.8111|-79.3976
VA|045|RNK|Campbell|VA045|Campbell|51031|E|cc|37.2231|-79.1048
VA|045|RNK|Campbell|VA045|City of Lynchburg|51680|E|cc|37.2231|-79.1048
VA|046|RNK|Appomattox|VA046|Appomattox|51011|E|cc|37.3722|-78.8121
VA|047|RNK|Buckingham|VA047|Buckingham|51029|E|cc|37.5722|-78.5287
VA|058|RNK|Halifax|VA058|Halifax|51083|E|sc|36.767|-78.9367
VA|059|RNK|Charlotte|VA059|Charlotte|51037|E|sc|37.0116|-78.6616
VA|508|RNK|Central Virginia Blue Ridge|VA508|Amherst|51009|E|cc|37.9889|-78.9469
VA|508|RNK|Central Virginia Blue Ridge|VA508|Nelson|51125|E|cc|37.9889|-78.9469
VA|508|RNK|Central Virginia Blue Ridge|VA508|Rockbridge|51163|E|wc|37.9889|-78.9469
WV|042|RNK|Mercer|WV042|Mercer|54055|E|se|37.4055|-81.1114
WV|043|RNK|Summers|WV043|Summers|54089|E|se|37.6559|-80.8586
WV|044|RNK|Monroe|WV044|Monroe|54063|E|se|37.5604|-80.5505
WV|507|RNK|Eastern Greenbrier|WV507|Greenbrier|54025|E|se|38.6434|-79.2919
WV|508|RNK|Western Greenbrier|WV508|Greenbrier|54025|E|se|37.9469|-80.4529
WA|001|SEW|San Juan County|WA001|San Juan|53055|P|nw|48.5786|-122.9627
WA|503|SEW|Western Whatcom County|WA503|Whatcom|53073|P|nw|48.8588|-122.4772
WA|504|SEW|Southwest Interior|WA504|Lewis|53041|P|wc|46.7206|-122.8973
WA|504|SEW|Southwest Interior|WA504|Thurston|53067|P|wc|46.7206|-122.8973
WA|506|SEW|Western Skagit County|WA506|Skagit|53057|P|nw|48.4646|-122.3668
WA|507|SEW|Everett and Vicinity|WA507|Kitsap|53035|P|wc|48.0549|-122.2545
WA|507|SEW|Everett and Vicinity|WA507|Snohomish|53061|P|wc|48.0549|-122.2545
WA|509|SEW|Tacoma Area|WA509|Pierce|53053|P|wc|47.1703|-122.5041
WA|510|SEW|Admiralty Inlet Area|WA510|Island|53029|P|nw|48.1131|-122.6404
WA|510|SEW|Admiralty Inlet Area|WA510|Jefferson|53031|P|nw|48.1131|-122.6404
WA|511|SEW|Hood Canal Area|WA511|Jefferson|53031|P|nw|47.4978|-122.967
WA|511|SEW|Hood Canal Area|WA511|Kitsap|53035|P|wc|47.4978|-122.967
WA|511|SEW|Hood Canal Area|WA511|Mason|53045|P|wc|47.4978|-122.967
WA|512|SEW|Lower Chehalis Valley Area|WA512|Grays Harbor|53027|P|ww|47.0579|-123.5111
WA|512|SEW|Lower Chehalis Valley Area|WA512|Mason|53045|P|wc|47.0579|-123.5111
WA|513|SEW|Olympics|WA513|Clallam|53009|P|nw|47.7525|-123.599
WA|513|SEW|Olympics|WA513|Grays Harbor|53027|P|ww|47.7525|-123.599
WA|513|SEW|Olympics|WA513|Jefferson|53031|P|nw|47.7525|-123.599
WA|513|SEW|Olympics|WA513|Mason|53045|P|wc|47.7525|-123.599
WA|514|SEW|Eastern Strait of Juan de Fuca|WA514|Clallam|53009|P|nw|48.076|-123.2615
WA|515|SEW|Western Strait of Juan De Fuca|WA515|Clallam|53009|P|nw|48.1845|-124.1477
WA|516|SEW|North Coast|WA516|Clallam|53009|P|nw|47.9309|-124.4066
WA|516|SEW|North Coast|WA516|Jefferson|53031|P|nw|47.9309|-124.4066
WA|517|SEW|Central Coast|WA517|Grays Harbor|53027|P|ww|47.1902|-124.0272
WA|555|SEW|East Puget Sound Lowlands|WA555|King|53033|P|wc|47.562|-122.0265
WA|555|SEW|East Puget Sound Lowlands|WA555|Pierce|53053|P|wc|47.562|-122.0265
WA|555|SEW|East Puget Sound Lowlands|WA555|Snohomish|53061|P|wc|48.0549|-122.2545
WA|556|SEW|Bellevue and Vicinity|WA556|King|53033|P|wc|47.521|-122.4499
WA|556|SEW|Bellevue and Vicinity|WA556|Snohomish|53061|P|wc|47.562|-122.0265
WA|558|SEW|Seattle and Vicinity|WA558|King|53033|P|wc|47.521|-122.4499
WA|559|SEW|Bremerton and Vicinity|WA559|Kitsap|53035|P|wc|47.4978|-122.967
WA|567|SEW|West Slopes North Cascades and Passes|WA567|Skagit|53057|P|nw|48.4646|-122.3668
WA|567|SEW|West Slopes North Cascades and Passes|WA567|Whatcom|53073|P|nw|48.8588|-122.4772
WA|568|SEW|West Slopes North Central Cascdes|WA568|King|53033|P|wc|47.562|-122.0265
WA|568|SEW|West Slopes North Central Cascdes|WA568|Snohomish|53061|P|wc|48.0549|-122.2545
WA|569|SEW|West Slopes South Central Cascades and Passes|WA569|Lewis|53041|P|wc|46.7206|-122.8973
WA|569|SEW|West Slopes South Central Cascades and Passes|WA569|Pierce|53053|P|wc|47.562|-122.0265
KS|073|SGF|Bourbon|KS073|Bourbon|20011|C|se|37.8552|-94.8493
KS|097|SGF|Crawford|KS097|Crawford|20037|C|se|37.5073|-94.8518
KS|101|SGF|Cherokee|KS101|Cherokee|20021|C|se|37.1693|-94.8462
MO|055|SGF|Benton|MO055|Benton|29015|C|cc|38.2948|-93.2879
MO|056|SGF|Morgan|MO056|Morgan|29141|C|cc|38.4239|-92.8861
MO|057|SGF|Miller|MO057|Miller|29131|C|cc|38.2145|-92.4284
MO|058|SGF|Maries|MO058|Maries|29125|C|cc|38.1616|-91.9249
MO|066|SGF|Vernon|MO066|Vernon|29217|C|wc|37.8506|-94.3424
MO|067|SGF|St. Clair|MO067|St. Clair|29185|C|wc|38.0371|-93.776
MO|068|SGF|Hickory|MO068|Hickory|29085|C|cc|37.9408|-93.3207
MO|069|SGF|Camden|MO069|Camden|29029|C|cc|38.0271|-92.766
MO|070|SGF|Pulaski|MO070|Pulaski|29169|C|cc|37.8246|-92.2076
MO|071|SGF|Phelps|MO071|Phelps|29161|C|ec|37.8771|-91.7924
MO|077|SGF|Barton|MO077|Barton|29011|C|sw|37.5023|-94.3471
MO|078|SGF|Cedar|MO078|Cedar|29039|C|sw|37.7238|-93.8566
MO|079|SGF|Polk|MO079|Polk|29167|C|sw|37.6165|-93.4005
MO|080|SGF|Dallas|MO080|Dallas|29059|C|sw|37.6804|-93.0236
MO|081|SGF|Laclede|MO081|Laclede|29105|C|sw|37.6583|-92.5903
MO|082|SGF|Texas|MO082|Texas|29215|C|sc|37.3173|-91.9651
MO|083|SGF|Dent|MO083|Dent|29065|C|sc|37.6066|-91.5079
MO|088|SGF|Jasper|MO088|Jasper|29097|C|sw|37.2035|-94.3406
MO|089|SGF|Dade|MO089|Dade|29057|C|sw|37.432|-93.8503
MO|090|SGF|Greene|MO090|Greene|29077|C|sw|37.2581|-93.342
MO|091|SGF|Webster|MO091|Webster|29225|C|sw|37.2809|-92.8759
MO|092|SGF|Wright|MO092|Wright|29229|C|sw|37.2701|-92.4687
MO|093|SGF|Newton|MO093|Newton|29145|C|sw|36.9055|-94.3392
MO|094|SGF|Lawrence|MO094|Lawrence|29109|C|sw|37.1064|-93.8329
MO|095|SGF|Christian|MO095|Christian|29043|C|sw|36.9696|-93.1889
MO|096|SGF|Douglas|MO096|Douglas|29067|C|sw|36.9326|-92.4988
MO|097|SGF|Howell|MO097|Howell|29091|C|sc|36.774|-91.8865
MO|098|SGF|Shannon|MO098|Shannon|29203|C|sc|37.1574|-91.4005
MO|101|SGF|McDonald|MO101|McDonald|29119|C|sw|36.6287|-94.3484
MO|102|SGF|Barry|MO102|Barry|29009|C|sw|36.7099|-93.8291
MO|103|SGF|Stone|MO103|Stone|29209|C|sw|36.7469|-93.4559
MO|104|SGF|Taney|MO104|Taney|29213|C|sw|36.6547|-93.041
MO|105|SGF|Ozark|MO105|Ozark|29153|C|sw|36.6493|-92.4446
MO|106|SGF|Oregon|MO106|Oregon|29149|C|sc|36.6867|-91.4033
CA|043|SGX|San Diego County Coastal Areas|CA043|San Diego|06073|P|sw|32.9783|-117.2367
CA|048|SGX|San Bernardino and Riverside County Valleys -The Inland Empire|CA048|Riverside|06065|P|ss|33.8486|-117.2412
CA|048|SGX|San Bernardino and Riverside County Valleys -The Inland Empire|CA048|San Bernardino|06071|P|ss|33.8486|-117.2412
CA|050|SGX|San Diego County Valleys|CA050|San Diego|06073|P|sw|33.0047|-116.9604
CA|055|SGX|San Bernardino County Mountains|CA055|San Bernardino|06071|P|ss|34.2304|-117.0957
CA|056|SGX|Riverside County Mountains|CA056|Riverside|06065|P|ss|33.66|-116.6434
CA|057|SGX|Santa Ana Mountains and Foothills|CA057|Orange|06059|P|sw|33.6256|-117.455
CA|057|SGX|Santa Ana Mountains and Foothills|CA057|Riverside|06065|P|ss|33.6256|-117.455
CA|057|SGX|Santa Ana Mountains and Foothills|CA057|San Diego|06073|P|sw|33.6256|-117.455
CA|058|SGX|San Diego County Mountains|CA058|San Diego|06073|P|sw|33.0713|-116.5324
CA|060|SGX|Apple and Lucerne Valleys|CA060|San Bernardino|06071|P|ss|34.5427|-117.0143
CA|061|SGX|Coachella Valley|CA061|Riverside|06065|P|ss|33.7424|-116.3024
CA|062|SGX|San Diego County Deserts|CA062|San Diego|06073|P|sw|33.0511|-116.2536
CA|065|SGX|San Gorgonio Pass Near Banning|CA065|Riverside|06065|P|ss|33.7185|-115.2342
CA|552|SGX|Orange County Coastal|CA552|Orange|06059|P|sw|33.7028|-117.7899
CA|554|SGX|Orange County Inland|CA554|Orange|06059|P|sw|33.7234|-117.7705
AR|050|SHV|Sevier|AR050|Sevier|05133|C|sw|33.9973|-94.2412
AR|051|SHV|Howard|AR051|Howard|05061|C|sw|34.0887|-93.9934
AR|059|SHV|Little River|AR059|Little River|05081|C|sw|33.7005|-94.2343
AR|060|SHV|Hempstead|AR060|Hempstead|05057|C|sw|33.7354|-93.6684
AR|061|SHV|Nevada|AR061|Nevada|05099|C|sw|33.6641|-93.3072
AR|070|SHV|Miller|AR070|Miller|05091|C|sw|33.3124|-93.8918
AR|071|SHV|Lafayette|AR071|Lafayette|05073|C|sw|33.2408|-93.6073
AR|072|SHV|Columbia|AR072|Columbia|05027|C|sw|33.2143|-93.2273
AR|073|SHV|Union|AR073|Union|05139|C|sc|33.1713|-92.5973
LA|001|SHV|Caddo|LA001|Caddo|22017|C|nw|32.5797|-93.8821
LA|002|SHV|Bossier|LA002|Bossier|22015|C|nw|32.6794|-93.6052
LA|003|SHV|Webster|LA003|Webster|22119|C|nw|32.7135|-93.335
LA|004|SHV|Claiborne|LA004|Claiborne|22027|C|nw|32.8226|-92.9957
LA|005|SHV|Lincoln|LA005|Lincoln|22061|C|nc|32.6016|-92.6647
LA|006|SHV|Union|LA006|Union|22111|C|nc|32.8319|-92.3748
LA|010|SHV|De Soto|LA010|De Soto|22031|C|nw|32.0554|-93.7373
LA|011|SHV|Red River|LA011|Red River|22081|C|nw|32.0933|-93.34
LA|012|SHV|Bienville|LA012|Bienville|22013|C|nw|32.3472|-93.056
LA|013|SHV|Jackson|LA013|Jackson|22049|C|nc|32.302|-92.5577
LA|014|SHV|Ouachita|LA014|Ouachita|22073|C|nc|32.4785|-92.1545
LA|017|SHV|Sabine|LA017|Sabine|22085|C|nw|31.564|-93.5547
LA|018|SHV|Natchitoches|LA018|Natchitoches|22069|C|nw|31.7236|-93.0963
LA|019|SHV|Winn|LA019|Winn|22127|C|nc|31.9442|-92.6368
LA|020|SHV|Grant|LA020|Grant|22043|C|nc|31.5997|-92.5594
LA|021|SHV|Caldwell|LA021|Caldwell|22021|C|nc|32.0922|-92.1167
LA|022|SHV|La Salle|LA022|La Salle|22059|C|nc|31.6767|-92.1604
OK|077|SHV|McCurtain|OK077|McCurtain|40089|C|se|34.1151|-94.7712
TX|096|SHV|Red River|TX096|Red River|48387|C|ne|33.6207|-95.0504
TX|097|SHV|Bowie|TX097|Bowie|48037|C|ne|33.4454|-94.4229
TX|108|SHV|Franklin|TX108|Franklin|48159|C|ne|33.1756|-95.2184
TX|109|SHV|Titus|TX109|Titus|48449|C|ne|33.2166|-94.9657
TX|110|SHV|Camp|TX110|Camp|48063|C|ne|32.9732|-94.9785
TX|111|SHV|Morris|TX111|Morris|48343|C|ne|33.1135|-94.7326
TX|112|SHV|Cass|TX112|Cass|48067|C|ne|33.0775|-94.3436
TX|124|SHV|Wood|TX124|Wood|48499|C|ne|32.7864|-95.3821
TX|125|SHV|Upshur|TX125|Upshur|48459|C|ne|32.7363|-94.9414
TX|126|SHV|Marion|TX126|Marion|48315|C|ne|32.798|-94.3572
TX|136|SHV|Smith|TX136|Smith|48423|C|ne|32.375|-95.2692
TX|137|SHV|Gregg|TX137|Gregg|48183|C|ne|32.4803|-94.8172
TX|138|SHV|Harrison|TX138|Harrison|48203|C|ne|32.5483|-94.3713
TX|149|SHV|Cherokee|TX149|Cherokee|48073|C|ne|31.837|-95.1652
TX|150|SHV|Rusk|TX150|Rusk|48401|C|ne|32.1077|-94.7618
TX|151|SHV|Panola|TX151|Panola|48365|C|ne|32.1624|-94.3056
TX|152|SHV|Nacogdoches|TX152|Nacogdoches|48347|C|ee|31.616|-94.6158
TX|153|SHV|Shelby|TX153|Shelby|48419|C|ee|31.7924|-94.145
TX|165|SHV|Angelina|TX165|Angelina|48005|C|ee|31.2548|-94.6118
TX|166|SHV|San Augustine|TX166|San Augustine|48405|C|ee|31.3942|-94.1682
TX|167|SHV|Sabine|TX167|Sabine|48403|C|ee|31.3432|-93.8518
TX|049|SJT|Fisher|TX049|Fisher|48151|C|nw|32.7428|-100.4022
TX|054|SJT|Nolan|TX054|Nolan|48353|C|nw|32.3035|-100.4061
TX|064|SJT|Sterling|TX064|Sterling|48431|C|sw|31.8279|-101.05
TX|065|SJT|Coke|TX065|Coke|48081|C|sw|31.8885|-100.5299
TX|066|SJT|Runnels|TX066|Runnels|48399|C|sw|31.8311|-99.9762
TX|071|SJT|Irion|TX071|Irion|48235|C|sw|31.3039|-100.9824
TX|072|SJT|Tom Green|TX072|Tom Green|48451|C|sw|31.4044|-100.4621
TX|073|SJT|Concho|TX073|Concho|48095|C|sw|31.3265|-99.864
TX|076|SJT|Crockett|TX076|Crockett|48105|C|sw|30.723|-101.4121
TX|077|SJT|Schleicher|TX077|Schleicher|48413|C|sw|30.8975|-100.5385
TX|078|SJT|Sutton|TX078|Sutton|48435|C|sw|30.4983|-100.5382
TX|098|SJT|Haskell|TX098|Haskell|48207|C|nc|33.1782|-99.7303
TX|099|SJT|Throckmorton|TX099|Throckmorton|48447|C|nc|33.1775|-99.2124
TX|113|SJT|Jones|TX113|Jones|48253|C|nc|32.7399|-99.8787
TX|114|SJT|Shackelford|TX114|Shackelford|48417|C|nc|32.736|-99.3541
TX|127|SJT|Taylor|TX127|Taylor|48441|C|nc|32.3015|-99.8901
TX|128|SJT|Callahan|TX128|Callahan|48059|C|nc|32.2977|-99.3735
TX|139|SJT|Coleman|TX139|Coleman|48083|C|nc|31.7732|-99.4536
TX|140|SJT|Brown|TX140|Brown|48049|C|nc|31.7743|-98.9998
TX|154|SJT|McCulloch|TX154|McCulloch|48307|C|nc|31.1989|-99.3475
TX|155|SJT|San Saba|TX155|San Saba|48411|C|nc|31.1552|-98.8176
TX|168|SJT|Menard|TX168|Menard|48327|C|sc|30.8898|-99.8206
TX|169|SJT|Kimble|TX169|Kimble|48267|C|sc|30.4868|-99.7487
TX|170|SJT|Mason|TX170|Mason|48319|C|sc|30.7177|-99.2261
PR|001|SJU|San Juan and Vicinity|PR001|Bayamon|72021|V||18.371|-66.0981
PR|001|SJU|San Juan and Vicinity|PR001|Carolina|72031|V||18.371|-66.0981
PR|001|SJU|San Juan and Vicinity|PR001|Catano|72033|V||18.371|-66.0981
PR|001|SJU|San Juan and Vicinity|PR001|Guaynabo|72061|V||18.371|-66.0981
PR|001|SJU|San Juan and Vicinity|PR001|San Juan|72127|V||18.371|-66.0981
PR|001|SJU|San Juan and Vicinity|PR001|Toa Alta|72135|V||18.371|-66.0981
PR|001|SJU|San Juan and Vicinity|PR001|Toa Baja|72137|V||18.371|-66.0981
PR|001|SJU|San Juan and Vicinity|PR001|Trujillo Alto|72139|V||18.371|-66.0981
PR|002|SJU|Northeast|PR002|Canovanas|72029|V||18.2861|-65.7796
PR|002|SJU|Northeast|PR002|Ceiba|72037|V||18.2861|-65.7796
PR|002|SJU|Northeast|PR002|Fajardo|72053|V||18.2861|-65.7796
PR|002|SJU|Northeast|PR002|Humacao|72069|V||18.2861|-65.7796
PR|002|SJU|Northeast|PR002|Loiza|72087|V||18.2861|-65.7796
PR|002|SJU|Northeast|PR002|Luquillo|72089|V||18.2861|-65.7796
PR|002|SJU|Northeast|PR002|Naguabo|72103|V||18.2861|-65.7796
PR|002|SJU|Northeast|PR002|Rio Grande|72119|V||18.2861|-65.7796
PR|003|SJU|Southeast|PR003|Arroyo|72015|V||18.0258|-66.0756
PR|003|SJU|Southeast|PR003|Guayama|72057|V||18.0258|-66.0756
PR|003|SJU|Southeast|PR003|Maunabo|72095|V||18.0258|-66.0756
PR|003|SJU|Southeast|PR003|Patillas|72109|V||18.0258|-66.0756
PR|003|SJU|Southeast|PR003|Salinas|72123|V||18.0258|-66.0756
PR|003|SJU|Southeast|PR003|Yabucoa|72151|V||18.0258|-66.0756
PR|004|SJU|Eastern Interior|PR004|Aguas Buenas|72007|V||18.1894|-66.052
PR|004|SJU|Eastern Interior|PR004|Caguas|72025|V||18.1894|-66.052
PR|004|SJU|Eastern Interior|PR004|Cayey|72035|V||18.1894|-66.052
PR|004|SJU|Eastern Interior|PR004|Cidra|72041|V||18.1894|-66.052
PR|004|SJU|Eastern Interior|PR004|Comerio|72045|V||18.1894|-66.052
PR|004|SJU|Eastern Interior|PR004|Gurabo|72063|V||18.1894|-66.052
PR|004|SJU|Eastern Interior|PR004|Juncos|72077|V||18.1894|-66.052
PR|004|SJU|Eastern Interior|PR004|Las Piedras|72085|V||18.1894|-66.052
PR|004|SJU|Eastern Interior|PR004|San Lorenzo|72129|V||18.1894|-66.052
PR|005|SJU|North Central|PR005|Arecibo|72013|V||18.4154|-66.5309
PR|005|SJU|North Central|PR005|Barceloneta|72017|V||18.4154|-66.5309
PR|005|SJU|North Central|PR005|Dorado|72051|V||18.4154|-66.5309
PR|005|SJU|North Central|PR005|Florida|72054|V||18.4154|-66.5309
PR|005|SJU|North Central|PR005|Manati|72091|V||18.4154|-66.5309
PR|005|SJU|North Central|PR005|Vega Alta|72143|V||18.4154|-66.5309
PR|005|SJU|North Central|PR005|Vega Baja|72145|V||18.4154|-66.5309
PR|006|SJU|Central Interior|PR006|Aibonito|72009|V||18.213|-66.4092
PR|006|SJU|Central Interior|PR006|Barranquitas|72019|V||18.213|-66.4092
PR|006|SJU|Central Interior|PR006|Ciales|72039|V||18.213|-66.4092
PR|006|SJU|Central Interior|PR006|Coamo|72043|V||18.213|-66.4092
PR|006|SJU|Central Interior|PR006|Corozal|72047|V||18.213|-66.4092
PR|006|SJU|Central Interior|PR006|Jayuya|72073|V||18.213|-66.4092
PR|006|SJU|Central Interior|PR006|Morovis|72101|V||18.213|-66.4092
PR|006|SJU|Central Interior|PR006|Naranjito|72105|V||18.213|-66.4092
PR|006|SJU|Central Interior|PR006|Orocovis|72107|V||18.213|-66.4092
PR|006|SJU|Central Interior|PR006|Villalba|72149|V||18.213|-66.4092
PR|007|SJU|Ponce and Vicinity|PR007|Guayanilla|72059|V||18.0539|-66.6527
PR|007|SJU|Ponce and Vicinity|PR007|Juana Diaz|72075|V||18.0539|-66.6527
PR|007|SJU|Ponce and Vicinity|PR007|Penuelas|72111|V||18.0539|-66.6527
PR|007|SJU|Ponce and Vicinity|PR007|Ponce|72113|V||18.0539|-66.6527
PR|007|SJU|Ponce and Vicinity|PR007|Santa Isabel|72133|V||18.0539|-66.6527
PR|007|SJU|Ponce and Vicinity|PR007|Yauco|72153|V||18.0539|-66.6527
PR|008|SJU|Northwest|PR008|Aguadilla|72005|V||18.4353|-66.941
PR|008|SJU|Northwest|PR008|Camuy|72027|V||18.4353|-66.941
PR|008|SJU|Northwest|PR008|Hatillo|72065|V||18.4353|-66.941
PR|008|SJU|Northwest|PR008|Isabela|72071|V||18.4353|-66.941
PR|008|SJU|Northwest|PR008|Quebradillas|72115|V||18.4353|-66.941
PR|009|SJU|Western Interior|PR009|Adjuntas|72001|V||18.2385|-66.8482
PR|009|SJU|Western Interior|PR009|Lares|72081|V||18.2385|-66.8482
PR|009|SJU|Western Interior|PR009|Las Marias|72083|V||18.2385|-66.8482
PR|009|SJU|Western Interior|PR009|Maricao|72093|V||18.2385|-66.8482
PR|009|SJU|Western Interior|PR009|Sabana Grande|72121|V||18.2385|-66.8482
PR|009|SJU|Western Interior|PR009|San Sebastian|72131|V||18.2385|-66.8482
PR|009|SJU|Western Interior|PR009|Utuado|72141|V||18.2385|-66.8482
PR|010|SJU|Mayaguez and Vicinity|PR010|Aguada|72003|V||18.2425|-67.1683
PR|010|SJU|Mayaguez and Vicinity|PR010|Anasco|72011|V||18.2425|-67.1683
PR|010|SJU|Mayaguez and Vicinity|PR010|Hormigueros|72067|V||18.2425|-67.1683
PR|010|SJU|Mayaguez and Vicinity|PR010|Mayaguez|72097|V||18.2425|-67.1683
PR|010|SJU|Mayaguez and Vicinity|PR010|Moca|72099|V||18.2425|-67.1683
PR|010|SJU|Mayaguez and Vicinity|PR010|Rincon|72117|V||18.2425|-67.1683
PR|010|SJU|Mayaguez and Vicinity|PR010|San German|72125|V||18.2425|-67.1683
PR|011|SJU|Southwest|PR011|Cabo Rojo|72023|V||18.018|-67.0614
PR|011|SJU|Southwest|PR011|Guanica|72055|V||18.018|-67.0614
PR|011|SJU|Southwest|PR011|Lajas|72079|V||18.018|-67.0614
PR|012|SJU|Culebra|PR012|Culebra|72049|V||18.3159|-65.2877
PR|013|SJU|Vieques|PR013|Vieques|72147|V||18.1231|-65.4415
VI|001|SJU|St.Thomas...St. John.. and Adjacent Islands|VI001|Saint John|78020|V||18.3429|-64.8564
VI|001|SJU|St.Thomas...St. John.. and Adjacent Islands|VI001|Saint Thomas|78030|V||18.3429|-64.8564
VI|002|SJU|St Croix|VI002|Saint Croix|78010|V||17.7333|-64.7677
UT|101|SLC|Great Salt Lake Desert and Mountains|UT101|Box Elder|49003|M|nn|40.9292|-113.2347
UT|101|SLC|Great Salt Lake Desert and Mountains|UT101|Salt Lake|49035|M|nn|40.9292|-113.2347
UT|101|SLC|Great Salt Lake Desert and Mountains|UT101|Tooele|49045|M|nn|40.9292|-113.2347
UT|101|SLC|Great Salt Lake Desert and Mountains|UT101|Utah|49049|M|nn|40.9292|-113.2347
UT|102|SLC|Tooele and Rush Valleys|UT102|Tooele|49045|M|nn|40.3692|-112.3841
UT|103|SLC|Eastern Box Elder County|UT103|Box Elder|49003|M|nn|41.71|-112.322
UT|104|SLC|Northern Wasatch Front|UT104|Davis|49011|M|nn|41.0742|-112.1496
UT|104|SLC|Northern Wasatch Front|UT104|Weber|49057|M|nn|41.0742|-112.1496
UT|105|SLC|Salt Lake Valley|UT105|Salt Lake|49035|M|nn|40.6778|-111.9881
UT|106|SLC|Utah Valley|UT106|Utah|49049|M|nn|40.1571|-111.9
UT|107|SLC|Cache Valley/Utah Portion|UT107|Cache|49005|M|nn|41.809|-111.9092
UT|108|SLC|Wasatch Back|UT108|Morgan|49029|M|nn|40.8141|-111.5267
UT|108|SLC|Wasatch Back|UT108|Summit|49043|M|nn|40.8141|-111.5267
UT|108|SLC|Wasatch Back|UT108|Wasatch|49051|M|nn|40.8141|-111.5267
UT|108|SLC|Wasatch Back|UT108|Weber|49057|M|nn|40.8141|-111.5267
UT|109|SLC|Bear Lake and Bear River Valley|UT109|Rich|49033|M|nn|41.6797|-111.1912
UT|110|SLC|Wasatch Mountains I-80 North|UT110|Box Elder|49003|M|nn|41.4128|-111.546
UT|110|SLC|Wasatch Mountains I-80 North|UT110|Cache|49005|M|nn|41.4128|-111.546
UT|110|SLC|Wasatch Mountains I-80 North|UT110|Davis|49011|M|nn|41.4128|-111.546
UT|110|SLC|Wasatch Mountains I-80 North|UT110|Morgan|49029|M|nn|41.4128|-111.546
UT|110|SLC|Wasatch Mountains I-80 North|UT110|Rich|49033|M|nn|41.4128|-111.546
UT|110|SLC|Wasatch Mountains I-80 North|UT110|Salt Lake|49035|M|nn|41.4128|-111.546
UT|110|SLC|Wasatch Mountains I-80 North|UT110|Summit|49043|M|nn|41.4128|-111.546
UT|110|SLC|Wasatch Mountains I-80 North|UT110|Weber|49057|M|nn|41.4128|-111.546
UT|111|SLC|Wasatch Mountains South of I-80|UT111|Juab|49023|M|nn|40.2682|-111.62
UT|111|SLC|Wasatch Mountains South of I-80|UT111|Salt Lake|49035|M|nn|40.2682|-111.62
UT|111|SLC|Wasatch Mountains South of I-80|UT111|Summit|49043|M|nn|40.2682|-111.62
UT|111|SLC|Wasatch Mountains South of I-80|UT111|Utah|49049|M|nn|40.2682|-111.62
UT|111|SLC|Wasatch Mountains South of I-80|UT111|Wasatch|49051|M|nn|40.2682|-111.62
UT|112|SLC|Western Uinta Mountains|UT112|Duchesne|49013|M|nn|40.6923|-110.7334
UT|112|SLC|Western Uinta Mountains|UT112|Summit|49043|M|nn|40.6923|-110.7334
UT|112|SLC|Western Uinta Mountains|UT112|Wasatch|49051|M|nn|40.6923|-110.7334
UT|113|SLC|Wasatch Plateau/Book Cliffs|UT113|Carbon|49007|M|cc|39.8071|-110.767
UT|113|SLC|Wasatch Plateau/Book Cliffs|UT113|Duchesne|49013|M|cc|39.8071|-110.767
UT|113|SLC|Wasatch Plateau/Book Cliffs|UT113|Emery|49015|M|cc|39.8071|-110.767
UT|113|SLC|Wasatch Plateau/Book Cliffs|UT113|Sanpete|49039|M|cc|39.8071|-110.767
UT|113|SLC|Wasatch Plateau/Book Cliffs|UT113|Utah|49049|M|cc|39.8071|-110.767
UT|113|SLC|Wasatch Plateau/Book Cliffs|UT113|Wasatch|49051|M|cc|39.8071|-110.767
UT|114|SLC|Western Uinta Basin|UT114|Duchesne|49013|M|nn|40.246|-110.3145
UT|115|SLC|Western Millard and Juab Counties|UT115|Juab|49023|M|cc|39.307|-113.1813
UT|115|SLC|Western Millard and Juab Counties|UT115|Millard|49027|M|cc|39.307|-113.1813
UT|116|SLC|Eastern Juab/Millard Counties|UT116|Juab|49023|M|cc|39.2286|-112.2213
UT|116|SLC|Eastern Juab/Millard Counties|UT116|Millard|49027|M|cc|39.2286|-112.2213
UT|117|SLC|Central Mountains|UT117|Emery|49015|M|cc|39.0084|-111.7827
UT|117|SLC|Central Mountains|UT117|Juab|49023|M|cc|39.0084|-111.7827
UT|117|SLC|Central Mountains|UT117|Millard|49027|M|cc|39.0084|-111.7827
UT|117|SLC|Central Mountains|UT117|Sanpete|49039|M|cc|39.0084|-111.7827
UT|117|SLC|Central Mountains|UT117|Sevier|49041|M|cc|39.0084|-111.7827
UT|118|SLC|Sanpete Valley|UT118|Sanpete|49039|M|cc|39.3723|-111.6668
UT|119|SLC|Sevier Valley|UT119|Sevier|49041|M|cc|38.7785|-112.039
UT|120|SLC|Castle Country|UT120|Carbon|49007|M|cc|39.3174|-110.8905
UT|120|SLC|Castle Country|UT120|Emery|49015|M|cc|39.3174|-110.8905
UT|120|SLC|Castle Country|UT120|Sevier|49041|M|cc|39.3174|-110.8905
UT|121|SLC|San Rafael Swell|UT121|Emery|49015|M|cc|38.8704|-110.632
UT|121|SLC|San Rafael Swell|UT121|Sevier|49041|M|cc|38.8704|-110.632
UT|122|SLC|Southwest Utah|UT122|Beaver|49001|M|sw|38.1051|-113.4513
UT|122|SLC|Southwest Utah|UT122|Iron|49021|M|sw|38.1051|-113.4513
UT|122|SLC|Southwest Utah|UT122|Washington|49053|M|sw|38.1051|-113.4513
UT|123|SLC|Lower Washington County|UT123|Washington|49053|M|sw|37.1632|-113.6488
UT|124|SLC|Zion National Park|UT124|Iron|49021|M|sw|37.2808|-113.0793
UT|124|SLC|Zion National Park|UT124|Kane|49025|M|sw|37.2808|-113.0793
UT|124|SLC|Zion National Park|UT124|Washington|49053|M|sw|37.2808|-113.0793
UT|125|SLC|Southern Mountains|UT125|Beaver|49001|M|ss|37.8671|-112.4662
UT|125|SLC|Southern Mountains|UT125|Garfield|49017|M|ss|37.8671|-112.4662
UT|125|SLC|Southern Mountains|UT125|Iron|49021|M|ss|37.8671|-112.4662
UT|125|SLC|Southern Mountains|UT125|Kane|49025|M|ss|37.8671|-112.4662
UT|125|SLC|Southern Mountains|UT125|Piute|49031|M|ss|37.8671|-112.4662
UT|125|SLC|Southern Mountains|UT125|Washington|49053|M|ss|37.8671|-112.4662
UT|125|SLC|Southern Mountains|UT125|Wayne|49055|M|ss|37.8671|-112.4662
UT|126|SLC|Upper Sevier River Valleys|UT126|Garfield|49017|M|ss|38.1842|-112.1917
UT|126|SLC|Upper Sevier River Valleys|UT126|Piute|49031|M|ss|38.1842|-112.1917
UT|126|SLC|Upper Sevier River Valleys|UT126|Sevier|49041|M|ss|38.1842|-112.1917
UT|127|SLC|Bryce Canyon Country|UT127|Garfield|49017|M|ss|37.738|-112.1542
UT|127|SLC|Bryce Canyon Country|UT127|Kane|49025|M|ss|37.738|-112.1542
UT|128|SLC|South Central Utah|UT128|Garfield|49017|M|ss|37.3759|-111.8128
UT|128|SLC|South Central Utah|UT128|Kane|49025|M|ss|37.3759|-111.8128
UT|128|SLC|South Central Utah|UT128|Washington|49053|M|ss|37.3759|-111.8128
UT|129|SLC|Capitol Reef National Park and Vicinity|UT129|Emery|49015|M|ss|38.2218|-111.2634
UT|129|SLC|Capitol Reef National Park and Vicinity|UT129|Garfield|49017|M|ss|38.2218|-111.2634
UT|129|SLC|Capitol Reef National Park and Vicinity|UT129|Sevier|49041|M|ss|38.2218|-111.2634
UT|129|SLC|Capitol Reef National Park and Vicinity|UT129|Wayne|49055|M|ss|38.2218|-111.2634
UT|130|SLC|Western Canyonlands|UT130|Garfield|49017|M|ss|38.1697|-110.5783
UT|130|SLC|Western Canyonlands|UT130|Wayne|49055|M|ss|38.1697|-110.5783
UT|131|SLC|Glen Canyon Recreation Area/Lake Powell|UT131|Garfield|49017|M|se|37.3615|-110.7898
UT|131|SLC|Glen Canyon Recreation Area/Lake Powell|UT131|Kane|49025|M|se|37.3615|-110.7898
UT|131|SLC|Glen Canyon Recreation Area/Lake Powell|UT131|San Juan|49037|M|se|37.3615|-110.7898
WY|021|SLC|Southwest Wyoming|WY021|Uinta|56041|M|sw|41.2876|-110.5476
CA|013|STO|Shasta Lake Area / Northern Shasta County|CA013|Shasta|06089|P|nn|40.9299|-122.2247
CA|014|STO|Burney Basin / Eastern Shasta County|CA014|Shasta|06089|P|nn|40.9423|-121.4882
CA|015|STO|Northern Sacramento Valley|CA015|Shasta|06089|P|nn|40.2198|-122.2949
CA|015|STO|Northern Sacramento Valley|CA015|Tehama|06103|P|nn|40.2198|-122.2949
CA|016|STO|Central Sacramento Valley|CA016|Butte|06007|P|nn|39.3764|-121.926
CA|016|STO|Central Sacramento Valley|CA016|Colusa|06011|P|cc|39.3764|-121.926
CA|016|STO|Central Sacramento Valley|CA016|Glenn|06021|P|nn|39.3764|-121.926
CA|016|STO|Central Sacramento Valley|CA016|Nevada|06057|P|cc|39.3764|-121.926
CA|016|STO|Central Sacramento Valley|CA016|Sutter|06101|P|cc|39.3764|-121.926
CA|016|STO|Central Sacramento Valley|CA016|Yuba|06115|P|cc|39.3764|-121.926
CA|017|STO|Southern Sacramento Valley|CA017|Amador|06005|P|cc|38.6268|-121.5625
CA|017|STO|Southern Sacramento Valley|CA017|El Dorado|06017|P|cc|38.6268|-121.5625
CA|017|STO|Southern Sacramento Valley|CA017|Placer|06061|P|cc|38.6268|-121.5625
CA|017|STO|Southern Sacramento Valley|CA017|Sacramento|06067|P|cc|38.6268|-121.5625
CA|017|STO|Southern Sacramento Valley|CA017|Solano|06095|P|ww|38.6268|-121.5625
CA|017|STO|Southern Sacramento Valley|CA017|Sutter|06101|P|cc|38.6268|-121.5625
CA|017|STO|Southern Sacramento Valley|CA017|Yolo|06113|P|cc|38.6268|-121.5625
CA|018|STO|Carquinez Strait and Delta|CA018|Sacramento|06067|P|cc|38.1432|-121.7623
CA|018|STO|Carquinez Strait and Delta|CA018|San Joaquin|06077|P|cc|38.1432|-121.7623
CA|018|STO|Carquinez Strait and Delta|CA018|Solano|06095|P|ww|38.1432|-121.7623
CA|019|STO|Northern San Joaquin Valley|CA019|Amador|06005|P|cc|37.7581|-121.041
CA|019|STO|Northern San Joaquin Valley|CA019|Calaveras|06009|P|cc|37.7581|-121.041
CA|019|STO|Northern San Joaquin Valley|CA019|San Joaquin|06077|P|cc|37.7581|-121.041
CA|019|STO|Northern San Joaquin Valley|CA019|Stanislaus|06099|P|cc|37.7581|-121.041
CA|019|STO|Northern San Joaquin Valley|CA019|Tuolumne|06109|P|cc|37.7581|-121.041
CA|063|STO|Mountains Southwestern Shasta County to Western Colusa County|CA063|Colusa|06011|P|cc|39.8175|-122.7565
CA|063|STO|Mountains Southwestern Shasta County to Western Colusa County|CA063|Glenn|06021|P|nn|39.8175|-122.7565
CA|063|STO|Mountains Southwestern Shasta County to Western Colusa County|CA063|Shasta|06089|P|nn|39.8175|-122.7565
CA|063|STO|Mountains Southwestern Shasta County to Western Colusa County|CA063|Tehama|06103|P|nn|39.8175|-122.7565
CA|066|STO|Northeast Foothills/Sacramento Valley|CA066|Butte|06007|P|nn|40.1117|-121.7566
CA|066|STO|Northeast Foothills/Sacramento Valley|CA066|Shasta|06089|P|nn|40.1117|-121.7566
CA|066|STO|Northeast Foothills/Sacramento Valley|CA066|Tehama|06103|P|nn|40.1117|-121.7566
CA|067|STO|Motherlode|CA067|Amador|06005|P|cc|38.6192|-120.7698
CA|067|STO|Motherlode|CA067|Calaveras|06009|P|cc|38.6192|-120.7698
CA|067|STO|Motherlode|CA067|El Dorado|06017|P|cc|38.6192|-120.7698
CA|067|STO|Motherlode|CA067|Nevada|06057|P|cc|38.6192|-120.7698
CA|067|STO|Motherlode|CA067|Placer|06061|P|cc|38.6192|-120.7698
CA|067|STO|Motherlode|CA067|Tuolumne|06109|P|cc|38.6192|-120.7698
CA|067|STO|Motherlode|CA067|Yuba|06115|P|cc|38.6192|-120.7698
CA|068|STO|Western Plumas County/Lassen Park|CA068|Butte|06007|P|nn|40.1971|-121.3501
CA|068|STO|Western Plumas County/Lassen Park|CA068|Lassen|06035|P|nn|40.1971|-121.3501
CA|068|STO|Western Plumas County/Lassen Park|CA068|Plumas|06063|P|nn|40.1971|-121.3501
CA|068|STO|Western Plumas County/Lassen Park|CA068|Shasta|06089|P|nn|40.1971|-121.3501
CA|068|STO|Western Plumas County/Lassen Park|CA068|Tehama|06103|P|nn|40.1971|-121.3501
CA|069|STO|West Slope Northern Sierra Nevada|CA069|Alpine|06003|P|cc|38.7829|-120.3423
CA|069|STO|West Slope Northern Sierra Nevada|CA069|Amador|06005|P|cc|38.7829|-120.3423
CA|069|STO|West Slope Northern Sierra Nevada|CA069|Calaveras|06009|P|cc|38.7829|-120.3423
CA|069|STO|West Slope Northern Sierra Nevada|CA069|El Dorado|06017|P|cc|38.7829|-120.3423
CA|069|STO|West Slope Northern Sierra Nevada|CA069|Nevada|06057|P|cc|38.7829|-120.3423
CA|069|STO|West Slope Northern Sierra Nevada|CA069|Placer|06061|P|cc|38.7829|-120.3423
CA|069|STO|West Slope Northern Sierra Nevada|CA069|Sierra|06091|P|nn|38.7829|-120.3423
CA|069|STO|West Slope Northern Sierra Nevada|CA069|Tuolumne|06109|P|cc|38.7829|-120.3423
CA|069|STO|West Slope Northern Sierra Nevada|CA069|Yuba|06115|P|cc|38.7829|-120.3423
AL|065|TAE|Coffee|AL065|Coffee|01031|C|se|31.4026|-85.9882
AL|066|TAE|Dale|AL066|Dale|01045|C|se|31.4318|-85.611
AL|067|TAE|Henry|AL067|Henry|01067|C|se|31.5147|-85.2414
AL|068|TAE|Geneva|AL068|Geneva|01061|C|se|31.095|-85.839
AL|069|TAE|Houston|AL069|Houston|01069|C|se|31.1532|-85.3025
FL|007|TAE|North Walton|FL007|Walton|12131|C|pa|30.8499|-86.2133
FL|008|TAE|Central Walton|FL008|Walton|12131|C|pa|30.5928|-86.1117
FL|009|TAE|Holmes|FL009|Holmes|12059|C|pa|30.8679|-85.8143
FL|010|TAE|Washington|FL010|Washington|12133|C|pa|30.6107|-85.6653
FL|011|TAE|Jackson|FL011|Jackson|12063|C|pa|30.78|-84.9213
FL|011|TAE|Jackson|FL011|Jackson|12063|C|pa|30.7956|-85.2194
FL|012|TAE|Inland Bay|FL012|Bay|12005|C|pa|30.366|-85.5408
FL|013|TAE|Calhoun|FL013|Calhoun|12013|C|pa|30.4061|-85.1972
FL|014|TAE|Inland Gulf|FL014|Gulf|12045|CE|pa|29.9507|-85.1548
FL|014|TAE|Inland Gulf|FL014|Gulf|12045|CE|pa|30.0103|-85.211
FL|015|TAE|Inland Franklin|FL015|Franklin|12037|E|bb|29.9462|-84.8653
FL|016|TAE|Gadsden|FL016|Gadsden|12039|E|bb|30.5795|-84.6137
FL|017|TAE|Leon|FL017|Leon|12073|E|bb|30.4581|-84.2779
FL|018|TAE|Inland Jefferson|FL018|Jefferson|12065|E|bb|30.4578|-83.8865
FL|019|TAE|Madison|FL019|Madison|12079|E|bb|30.4442|-83.47
FL|026|TAE|Liberty|FL026|Liberty|12077|E|bb|30.2414|-84.8829
FL|027|TAE|Inland Wakulla|FL027|Wakulla|12129|E|bb|30.2017|-84.4474
FL|028|TAE|Inland Taylor|FL028|Taylor|12123|E|bb|30.0954|-83.5767
FL|029|TAE|Lafayette|FL029|Lafayette|12067|E|bb|29.9855|-83.1811
FL|034|TAE|Inland Dixie|FL034|Dixie|12029|E|bb|29.6711|-83.1235
FL|108|TAE|South Walton|FL108|Walton|12131|C|pa|30.4183|-86.171
FL|108|TAE|South Walton|FL108|Walton|12131|C|pa|30.4183|-86.171
FL|112|TAE|Coastal Bay|FL112|Bay|12005|E|pa|30.2213|-85.6654
FL|114|TAE|Coastal Gulf|FL114|Gulf|12045|CE|pa|29.8173|-85.2726
FL|115|TAE|Coastal Franklin|FL115|Franklin|12037|E|bb|29.8382|-84.7899
FL|118|TAE|Coastal Jefferson|FL118|Jefferson|12065|E|bb|30.1477|-84.0221
FL|127|TAE|Coastal Wakulla|FL127|Wakulla|12129|E|bb|30.0968|-84.3009
FL|128|TAE|Coastal Taylor|FL128|Taylor|12123|E|bb|29.9259|-83.6703
FL|134|TAE|Coastal Dixie|FL134|Dixie|12029|E|bb|29.4924|-83.2251
GA|120|TAE|Quitman|GA120|Quitman|13239|E|sw|31.8674|-85.0188
GA|121|TAE|Clay|GA121|Clay|13061|E|sw|31.6264|-84.9803
GA|122|TAE|Randolph|GA122|Randolph|13243|E|sw|31.7626|-84.7542
GA|123|TAE|Calhoun|GA123|Calhoun|13037|E|sw|31.5292|-84.6249
GA|124|TAE|Terrell|GA124|Terrell|13273|E|sw|31.7768|-84.4368
GA|125|TAE|Dougherty|GA125|Dougherty|13095|E|sw|31.5333|-84.2164
GA|126|TAE|Lee|GA126|Lee|13177|E|sw|31.7796|-84.141
GA|127|TAE|Worth|GA127|Worth|13321|E|sc|31.5515|-83.851
GA|128|TAE|Turner|GA128|Turner|13287|E|sc|31.7163|-83.6242
GA|129|TAE|Tift|GA129|Tift|13277|E|sc|31.4575|-83.5266
GA|130|TAE|Ben Hill|GA130|Ben Hill|13017|E|sc|31.7598|-83.2205
GA|131|TAE|Irwin|GA131|Irwin|13155|E|sc|31.6023|-83.2764
GA|142|TAE|Early|GA142|Early|13099|E|sw|31.3229|-84.9037
GA|143|TAE|Miller|GA143|Miller|13201|E|sw|31.164|-84.7307
GA|144|TAE|Baker|GA144|Baker|13007|E|sw|31.3262|-84.4447
GA|145|TAE|Mitchell|GA145|Mitchell|13205|E|sw|31.2254|-84.1942
GA|146|TAE|Colquitt|GA146|Colquitt|13071|E|sc|31.1884|-83.7688
GA|147|TAE|Cook|GA147|Cook|13075|E|sc|31.154|-83.4305
GA|148|TAE|Berrien|GA148|Berrien|13019|E|sc|31.2761|-83.2297
GA|155|TAE|Seminole|GA155|Seminole|13253|E|sw|30.9481|-84.8681
GA|156|TAE|Decatur|GA156|Decatur|13087|E|sw|30.7994|-84.7577
GA|156|TAE|Decatur|GA156|Decatur|13087|E|sw|30.8815|-84.572
GA|157|TAE|Grady|GA157|Grady|13131|E|sw|30.8747|-84.2344
GA|158|TAE|Thomas|GA158|Thomas|13275|E|sc|30.8637|-83.9194
GA|159|TAE|Brooks|GA159|Brooks|13027|E|sc|30.842|-83.5803
GA|160|TAE|Lowndes|GA160|Lowndes|13185|E|sc|30.8339|-83.2677
GA|161|TAE|Lanier|GA161|Lanier|13173|E|sc|31.038|-83.0626
FL|043|TBW|Sumter|FL043|Sumter|12119|E|cc|28.7046|-82.081
FL|050|TBW|Pinellas|FL050|Pinellas|12103|E|wc|27.9283|-82.7219
FL|052|TBW|Polk|FL052|Polk|12105|E|cc|27.9489|-81.6978
FL|056|TBW|Hardee|FL056|Hardee|12049|E|cc|27.4927|-81.8099
FL|057|TBW|Highlands|FL057|Highlands|12055|E|sc|27.3434|-81.3409
FL|061|TBW|De Soto|FL061|DeSoto|12027|E|sc|27.1863|-81.8093
FL|139|TBW|Coastal Levy|FL139|Levy|12075|E|nn|29.3216|-82.7385
FL|142|TBW|Coastal Citrus|FL142|Citrus|12017|E|wc|28.8507|-82.4673
FL|148|TBW|Coastal Hernando|FL148|Hernando|12053|E|wc|28.5528|-82.4209
FL|149|TBW|Inland Pasco|FL149|Pasco|12101|E|wc|28.3093|-82.3912
FL|151|TBW|Coastal Hillsborough|FL151|Hillsborough|12057|E|wc|27.9291|-82.4769
FL|155|TBW|Coastal Manatee|FL155|Manatee|12081|E|wc|27.4713|-82.2978
FL|160|TBW|Coastal Sarasota|FL160|Sarasota|12115|E|wc|27.1806|-82.3219
FL|162|TBW|Coastal Charlotte|FL162|Charlotte|12015|E|sw|26.9118|-82.1135
FL|165|TBW|Coastal Lee|FL165|Lee|12071|E|sw|26.6135|-81.8902
FL|239|TBW|Inland Levy|FL239|Levy|12075|E|nn|29.3216|-82.7385
FL|242|TBW|inland Citrus|FL242|Citrus|12017|E|wc|28.8507|-82.4673
FL|248|TBW|Inland Hernando|FL248|Hernando|12053|E|wc|28.5528|-82.4209
FL|249|TBW|Coastal Pasco|FL249|Pasco|12101|E|wc|28.3093|-82.3912
FL|251|TBW|Inland Hillsborough|FL251|Hillsborough|12057|E|wc|27.9311|-82.2469
FL|255|TBW|Inland Manatee|FL255|Manatee|12081|E|wc|27.4713|-82.2978
FL|260|TBW|Inland Sarasota|FL260|Sarasota|12115|E|wc|27.1806|-82.3219
FL|262|TBW|Inland Charlotte|FL262|Charlotte|12015|E|sw|26.9037|-81.7547
FL|265|TBW|Inland Lee|FL265|Lee|12071|E|sw|26.5785|-81.8208
MT|301|TFX|East Glacier Park Region|MT301|Glacier|30035|M|nc|48.6372|-113.422
MT|301|TFX|East Glacier Park Region|MT301|Pondera|30073|M|nc|48.6372|-113.422
MT|302|TFX|Northern High Plains|MT302|Glacier|30035|M|nc|48.5425|-112.8524
MT|302|TFX|Northern High Plains|MT302|Pondera|30073|M|nc|48.5425|-112.8524
MT|303|TFX|Eastern Glacier, Western Toole, and Central Pondera|MT303|Glacier|30035|M|nc|48.6453|-112.2726
MT|303|TFX|Eastern Glacier, Western Toole, and Central Pondera|MT303|Pondera|30073|M|nc|48.6453|-112.2726
MT|303|TFX|Eastern Glacier, Western Toole, and Central Pondera|MT303|Toole|30101|M|nc|48.6453|-112.2726
MT|304|TFX|Eastern Toole and Liberty|MT304|Toole|30101|M|nc|48.5958|-111.2827
MT|304|TFX|Eastern Toole and Liberty|MT304|Liberty|30051|M|nc|48.5958|-111.2827
MT|305|TFX|Hill County|MT305|Hill|30041|M|nc|48.6691|-110.1728
MT|306|TFX|Northern Blaine County|MT306|Blaine|30005|M|nc|48.7135|-108.8425
MT|307|TFX|Southern Rocky Mountain Front|MT307|Lewis and Clark|30049|M|nc|47.5101|-112.7733
MT|307|TFX|Southern Rocky Mountain Front|MT307|Teton|30099|M|nc|47.5101|-112.7733
MT|308|TFX|Southern High Plains|MT308|Lewis and Clark|30049|M|nc|47.6849|-112.3405
MT|308|TFX|Southern High Plains|MT308|Teton|30099|M|nc|47.6849|-112.3405
MT|309|TFX|Eastern Pondera and Eastern Teton|MT309|Pondera|30073|M|nc|47.9541|-111.7646
MT|309|TFX|Eastern Pondera and Eastern Teton|MT309|Teton|30099|M|nc|47.9541|-111.7646
MT|310|TFX|Western and Central Chouteau County|MT310|Chouteau|30015|M|nc|47.8751|-110.5845
MT|311|TFX|Bears Paw Mountains and Southern Blaine|MT311|Hill|30041|M|nc|48.1247|-109.3165
MT|311|TFX|Bears Paw Mountains and Southern Blaine|MT311|Blaine|30005|M|nc|48.1247|-109.3165
MT|311|TFX|Bears Paw Mountains and Southern Blaine|MT311|Chouteau|30015|M|nc|48.1247|-109.3165
MT|312|TFX|Cascade County below 5000ft|MT312|Cascade|30013|M|nc|47.4133|-111.3871
MT|313|TFX|Judith Basin County and Judith Gap|MT313|Judith Basin|30045|M|nc|47.098|-110.1395
MT|313|TFX|Judith Basin County and Judith Gap|MT313|Fergus|30027|M|nc|47.098|-110.1395
MT|314|TFX|Fergus County below 4500ft|MT314|Fergus|30027|M|nc|47.346|-109.2016
MT|315|TFX|Upper Blackfoot and MacDonald Pass|MT315|Lewis and Clark|30049|M|cc|46.806|-112.4247
MT|316|TFX|Gates of the Mountains|MT316|Lewis and Clark|30049|M|cc|47.0048|-111.9932
MT|316|TFX|Gates of the Mountains|MT316|Cascade|30013|M|cc|47.0048|-111.9932
MT|317|TFX|Little Belt and Highwood Mountains|MT317|Cascade|30013|M|cc|46.9742|-110.7705
MT|317|TFX|Little Belt and Highwood Mountains|MT317|Meagher|30059|M|cc|46.9742|-110.7705
MT|317|TFX|Little Belt and Highwood Mountains|MT317|Judith Basin|30045|M|cc|46.9742|-110.7705
MT|317|TFX|Little Belt and Highwood Mountains|MT317|Chouteau|30015|M|cc|46.9742|-110.7705
MT|318|TFX|Snowy and Judith Mountains|MT318|Fergus|30027|M|cc|46.9085|-109.2789
MT|319|TFX|Helena Valley|MT319|Lewis and Clark|30049|M|cc|46.6543|-111.9392
MT|320|TFX|Big Belt, Bridger and Castle Mountains|MT320|Lewis and Clark|30049|M|cc|46.3337|-111.1323
MT|320|TFX|Big Belt, Bridger and Castle Mountains|MT320|Broadwater|30007|M|cc|46.3337|-111.1323
MT|320|TFX|Big Belt, Bridger and Castle Mountains|MT320|Gallatin|30031|M|cc|46.3337|-111.1323
MT|320|TFX|Big Belt, Bridger and Castle Mountains|MT320|Meagher|30059|M|cc|46.3337|-111.1323
MT|321|TFX|Meagher County Valleys|MT321|Meagher|30059|M|cc|46.5176|-110.8308
MT|322|TFX|Elkhorn and Boulder Mountains|MT322|Jefferson|30043|M|cc|46.2336|-112.1068
MT|322|TFX|Elkhorn and Boulder Mountains|MT322|Broadwater|30007|M|cc|46.2336|-112.1068
MT|323|TFX|Canyon Ferry Area|MT323|Lewis and Clark|30049|M|cc|46.2952|-111.5425
MT|323|TFX|Canyon Ferry Area|MT323|Broadwater|30007|M|cc|46.2952|-111.5425
MT|324|TFX|Missouri Headwaters|MT324|Jefferson|30043|M|sw|45.8502|-111.8024
MT|324|TFX|Missouri Headwaters|MT324|Madison|30057|M|sw|45.8502|-111.8024
MT|324|TFX|Missouri Headwaters|MT324|Gallatin|30031|M|sw|45.8502|-111.8024
MT|325|TFX|Madison River Valley|MT325|Madison|30057|M|sw|45.3268|-111.6756
MT|326|TFX|Gallatin Valley|MT326|Gallatin|30031|M|sw|45.7532|-111.196
MT|327|TFX|Northwest Beaverhead County|MT327|Beaverhead|30001|M|sw|45.4903|-113.2984
MT|328|TFX|Beaverhead and Western Madison below 6000ft|MT328|Beaverhead|30001|M|sw|45.2964|-112.5631
MT|328|TFX|Beaverhead and Western Madison below 6000ft|MT328|Madison|30057|M|sw|45.2964|-112.5631
MT|329|TFX|Ruby Mountains and Southern Beaverhead Mountains|MT329|Beaverhead|30001|M|sw|44.8223|-112.6561
MT|329|TFX|Ruby Mountains and Southern Beaverhead Mountains|MT329|Madison|30057|M|sw|44.8223|-112.6561
MT|330|TFX|Gallatin and Madison County Mountains and Centennial Mountains|MT330|Beaverhead|30001|M|sw|45.0978|-111.6002
MT|330|TFX|Gallatin and Madison County Mountains and Centennial Mountains|MT330|Madison|30057|M|sw|45.0978|-111.6002
MT|330|TFX|Gallatin and Madison County Mountains and Centennial Mountains|MT330|Gallatin|30031|M|sw|45.0978|-111.6002
WY|001|TFX|Yellowstone National Park|WY001|Gallatin|30031|M|sw|44.5976|-110.5469
KS|008|TOP|Republic|KS008|Republic|20157|C|nc|39.8278|-97.6506
KS|009|TOP|Washington|KS009|Washington|20201|C|nc|39.7842|-97.0874
KS|010|TOP|Marshall|KS010|Marshall|20117|C|ne|39.7836|-96.5229
KS|011|TOP|Nemaha|KS011|Nemaha|20131|C|ne|39.7835|-96.0141
KS|012|TOP|Brown|KS012|Brown|20013|C|ne|39.8266|-95.5642
KS|020|TOP|Cloud|KS020|Cloud|20029|C|nc|39.4804|-97.6495
KS|021|TOP|Clay|KS021|Clay|20027|C|nc|39.3497|-97.1651
KS|022|TOP|Riley|KS022|Riley|20161|C|ne|39.2965|-96.7352
KS|023|TOP|Pottawatomie|KS023|Pottawatomie|20149|C|ne|39.379|-96.3425
KS|024|TOP|Jackson|KS024|Jackson|20085|C|ne|39.417|-95.7937
KS|026|TOP|Jefferson|KS026|Jefferson|20087|C|ne|39.2358|-95.3834
KS|034|TOP|Ottawa|KS034|Ottawa|20143|C|nc|39.1326|-97.6503
KS|035|TOP|Dickinson|KS035|Dickinson|20041|C|cc|38.8664|-97.1527
KS|036|TOP|Geary|KS036|Geary|20061|C|ec|39.0024|-96.7526
KS|037|TOP|Morris|KS037|Morris|20127|C|ec|38.6875|-96.6499
KS|038|TOP|Wabaunsee|KS038|Wabaunsee|20197|C|ec|38.9533|-96.205
KS|039|TOP|Shawnee|KS039|Shawnee|20177|C|ec|39.0415|-95.7564
KS|040|TOP|Douglas|KS040|Douglas|20045|C|ec|38.8845|-95.2924
KS|054|TOP|Lyon|KS054|Lyon|20111|C|ec|38.4563|-96.1527
KS|055|TOP|Osage|KS055|Osage|20139|C|ec|38.6524|-95.7269
KS|056|TOP|Franklin|KS056|Franklin|20059|C|ec|38.5646|-95.2859
KS|058|TOP|Coffey|KS058|Coffey|20031|C|ec|38.237|-95.7342
KS|059|TOP|Anderson|KS059|Anderson|20003|C|ec|38.2143|-95.2933
AR|001|TSA|Benton|AR001|Benton|05007|C|nw|36.3392|-94.2573
AR|002|TSA|Carroll|AR002|Carroll|05015|C|nw|36.341|-93.5382
AR|010|TSA|Washington|AR010|Washington|05143|C|nw|35.98|-94.2147
AR|011|TSA|Madison|AR011|Madison|05087|C|nw|36.011|-93.7246
AR|019|TSA|Crawford|AR019|Crawford|05033|C|nw|35.5889|-94.243
AR|020|TSA|Franklin|AR020|Franklin|05047|C|wc|35.5123|-93.8906
AR|029|TSA|Sebastian|AR029|Sebastian|05131|C|wc|35.1993|-94.274
OK|049|TSA|Pushmataha|OK049|Pushmataha|40127|C|se|34.4162|-95.3758
OK|053|TSA|Choctaw|OK053|Choctaw|40023|C|se|34.0265|-95.5521
OK|054|TSA|Osage|OK054|Osage|40113|C|ne|36.6292|-96.3984
OK|055|TSA|Washington|OK055|Washington|40147|C|ne|36.7152|-95.9044
OK|056|TSA|Nowata|OK056|Nowata|40105|C|ne|36.7985|-95.6175
OK|057|TSA|Craig|OK057|Craig|40035|C|ne|36.7617|-95.2085
OK|058|TSA|Ottawa|OK058|Ottawa|40115|C|ne|36.8355|-94.8105
OK|059|TSA|Pawnee|OK059|Pawnee|40117|C|ne|36.3169|-96.6993
OK|060|TSA|Tulsa|OK060|Tulsa|40143|C|ne|36.1211|-95.9415
OK|061|TSA|Rogers|OK061|Rogers|40131|C|ne|36.3716|-95.6044
OK|062|TSA|Mayes|OK062|Mayes|40097|C|ne|36.3018|-95.2309
OK|063|TSA|Delaware|OK063|Delaware|40041|C|ne|36.4082|-94.8027
OK|064|TSA|Creek|OK064|Creek|40037|C|ne|35.9027|-96.3709
OK|065|TSA|Okfuskee|OK065|Okfuskee|40107|C|ec|35.4655|-96.3228
OK|066|TSA|Okmulgee|OK066|Okmulgee|40111|C|ne|35.6467|-95.9643
OK|067|TSA|Wagoner|OK067|Wagoner|40145|C|ne|35.9609|-95.5212
OK|068|TSA|Cherokee|OK068|Cherokee|40021|C|ec|35.9066|-94.9997
OK|069|TSA|Adair|OK069|Adair|40001|C|ne|35.8839|-94.6587
OK|070|TSA|Muskogee|OK070|Muskogee|40101|C|ec|35.6161|-95.3794
OK|071|TSA|McIntosh|OK071|McIntosh|40091|C|se|35.3737|-95.6668
OK|072|TSA|Sequoyah|OK072|Sequoyah|40135|C|ec|35.4953|-94.7549
OK|073|TSA|Pittsburg|OK073|Pittsburg|40121|C|se|34.9239|-95.7484
OK|074|TSA|Haskell|OK074|Haskell|40061|C|se|35.2248|-95.1166
OK|075|TSA|Latimer|OK075|Latimer|40077|C|se|34.8761|-95.2504
OK|076|TSA|Le Flore|OK076|Le Flore|40079|C|se|34.9001|-94.7035
AZ|501|TWC|Western Pima County Including Ajo/Organ Pipe Cactus National Monument|AZ501|Pima|04019|m|sc|32.2167|-112.9766
AZ|502|TWC|Tohono O'odham Nation including Sells|AZ502|Pima|04019|m|sc|32.1434|-112.064
AZ|502|TWC|Tohono O'odham Nation including Sells|AZ502|Pinal|04021|m|sc|32.1434|-112.064
AZ|503|TWC|Upper Santa Cruz River and Altar Valleys including Nogales|AZ503|Pima|04019|m|sc|31.6207|-111.163
AZ|503|TWC|Upper Santa Cruz River and Altar Valleys including Nogales|AZ503|Santa Cruz|04023|m|se|31.6207|-111.163
AZ|504|TWC|Tucson Metro Area including Tucson/Green Valley/Marana/Vail|AZ504|Pima|04019|m|sc|32.1761|-111.0565
AZ|505|TWC|South Central Pinal County including Eloy/Picacho Peak State Park|AZ505|Pinal|04021|m|sc|32.7452|-111.3393
AZ|506|TWC|Southeast Pinal County including Kearny/Mammoth/Oracle|AZ506|Pinal|04021|m|sc|32.8255|-110.7518
AZ|507|TWC|Upper San Pedro River Valley including Sierra Vista/Benson|AZ507|Cochise|04003|m|se|31.9331|-110.3073
AZ|507|TWC|Upper San Pedro River Valley including Sierra Vista/Benson|AZ507|Graham|04009|m|se|31.9331|-110.3073
AZ|507|TWC|Upper San Pedro River Valley including Sierra Vista/Benson|AZ507|Pima|04019|m|sc|31.9331|-110.3073
AZ|507|TWC|Upper San Pedro River Valley including Sierra Vista/Benson|AZ507|Santa Cruz|04023|m|se|31.9331|-110.3073
AZ|508|TWC|Eastern Cochise County Below 5000 Feet including Douglas/Willcox|AZ508|Cochise|04003|m|se|31.9147|-109.5452
AZ|509|TWC|Upper Gila River and Aravaipa Valleys including Clifton/Safford|AZ509|Graham|04009|m|se|32.8686|-109.7443
AZ|509|TWC|Upper Gila River and Aravaipa Valleys including Clifton/Safford|AZ509|Greenlee|04011|m|se|32.8686|-109.7443
AZ|510|TWC|White Mountains of Graham and Greenlee Counties including Hannagan Meadow|AZ510|Graham|04009|m|se|33.3867|-109.4881
AZ|510|TWC|White Mountains of Graham and Greenlee Counties including Hannagan Meadow|AZ510|Greenlee|04011|m|se|33.3867|-109.4881
AZ|511|TWC|Galiuro and Pinaleno Mountains including Mount Graham|AZ511|Cochise|04003|m|se|32.6525|-110.1153
AZ|511|TWC|Galiuro and Pinaleno Mountains including Mount Graham|AZ511|Graham|04009|m|se|32.6525|-110.1153
AZ|511|TWC|Galiuro and Pinaleno Mountains including Mount Graham|AZ511|Pinal|04021|m|sc|32.6525|-110.1153
AZ|512|TWC|Chiricahua Mountains including Chiricahua National Monument|AZ512|Cochise|04003|m|se|31.8616|-109.356
AZ|513|TWC|Dragoon/Mule/Huachuca and Santa Rita Mountains including Bisbee/Canelo Hills/Madera Canyon|AZ513|Cochise|04003|m|se|31.6043|-110.3833
AZ|513|TWC|Dragoon/Mule/Huachuca and Santa Rita Mountains including Bisbee/Canelo Hills/Madera Canyon|AZ513|Pima|04019|m|sc|31.6043|-110.3833
AZ|513|TWC|Dragoon/Mule/Huachuca and Santa Rita Mountains including Bisbee/Canelo Hills/Madera Canyon|AZ513|Santa Cruz|04023|m|se|31.6043|-110.3833
AZ|514|TWC|Santa Catalina and Rincon Mountains including Mount Lemmon/Summerhaven|AZ514|Pima|04019|m|sc|32.3364|-110.6808
AZ|514|TWC|Santa Catalina and Rincon Mountains including Mount Lemmon/Summerhaven|AZ514|Pinal|04021|m|sc|32.3364|-110.6808
AZ|515|TWC|Baboquivari Mountains including Kitt Peak|AZ515|Pima|04019|m|sc|31.8186|-111.5931
SD|001|UNR|Harding|SD001|Harding|46063|M|nw|45.5804|-103.4959
SD|002|UNR|Northern Perkins |SD002|Perkins|46105|M|nw|45.7373|-102.4735
SD|012|UNR|Butte|SD012|Butte|46019|M|nw|44.9058|-103.5081
SD|013|UNR|Northern Meade Co Plains|SD013|Meade|46093|M|wc|44.8215|-102.48
SD|014|UNR|Ziebach|SD014|Ziebach|46137|M|wc|44.9806|-101.666
SD|024|UNR|Northern Black Hills |SD024|Lawrence|46081|M|wc|44.1987|-103.7924
SD|024|UNR|Northern Black Hills |SD024|Meade|46093|M|wc|44.1987|-103.7924
SD|024|UNR|Northern Black Hills |SD024|Pennington|46103|M|wc|44.1987|-103.7924
SD|025|UNR|Northern Foothills |SD025|Lawrence|46081|M|wc|44.5217|-103.7849
SD|026|UNR|Rapid City|SD026|Pennington|46103|M|wc|44.0007|-103.223
SD|027|UNR|Southern Foothills |SD027|Fall River|46047|M|sw|43.3817|-103.6039
SD|028|UNR|Central Black Hills |SD028|Pennington|46103|M|wc|43.8684|-103.6043
SD|028|UNR|Central Black Hills |SD028|Custer|46033|M|wc|43.8684|-103.6043
SD|029|UNR|Southern Black Hills |SD029|Custer|46033|M|sw|43.6072|-103.7517
SD|030|UNR|Custer Co Plains|SD030|Custer|46033|M|sw|43.6988|-102.9762
SD|031|UNR|Pennington Co Plains|SD031|Pennington|46103|M|wc|44.007|-102.4422
SD|032|UNR|Haakon|SD032|Haakon|46055|M|wc|44.2944|-101.5399
SD|041|UNR|Western Fall River |SD041|Fall River|46047|M|sw|43.171|-103.8148
SD|042|UNR|Northern Oglala Lakota |SD042|Oglala Lakota|46102|M|sw|43.5307|-102.5558
SD|043|UNR|Northern Jackson |SD043|Jackson|46071|M|sw|43.8677|-101.5949
SD|044|UNR|Bennett|SD044|Bennett|46007|M|sw|43.1949|-101.6639
SD|046|UNR|Mellette|SD046|Mellette|46095|C|sc|43.5811|-100.7601
SD|047|UNR|Todd|SD047|Todd|46121|C|sc|43.1934|-100.7184
SD|049|UNR|Tripp|SD049|Tripp|46123|C|sc|43.3459|-99.884
SD|072|UNR|Sturgis-Piedmont Foothills |SD072|Meade|46093|M|wc|44.3268|-103.3829
SD|073|UNR|Southern Meade Co Plains|SD073|Meade|46093|M|wc|44.4055|-102.7678
SD|074|UNR|Hermosa Foot Hills|SD074|Custer|46033|M|sw|43.6677|-103.2509
SD|075|UNR|Eastern Fall River |SD075|Fall River|46047|M|sw|43.2078|-103.2197
SD|076|UNR|Southern Oglala Lakota |SD076|Oglala Lakota|46102|M|sw|43.1901|-102.5485
SD|077|UNR|Southern Jackson |SD077|Jackson|46071|M|sw|43.5628|-101.6533
SD|078|UNR|Southern Perkins |SD078|Perkins|46105|M|nw|45.2845|-102.4779
WY|054|UNR|Northern Cambell|WY054|Campbell|56005|M|ne|44.596|-105.5497
WY|055|UNR|Southern Campbell|WY055|Campbell|56005|M|ne|43.8436|-105.5478
WY|056|UNR|Western Crook |WY056|Crook|56011|M|ne|44.6273|-104.8077
WY|057|UNR|Wyoming Black Hills |WY057|Crook|56011|M|ne|44.3823|-104.3495
WY|057|UNR|Wyoming Black Hills |WY057|Weston|56045|M|ne|44.3823|-104.3495
WY|058|UNR|Weston|WY058|Weston|56045|M|ne|43.8072|-104.6212
WY|058|UNR|Weston County Plains |WY058|Weston|56045|M|ne|43.8674|-104.7853
WY|059|UNR|Newcastle |WY059|Weston|56045|M|ne|43.7191|-104.3166
WY|060|UNR|Northeastern Crook |WY060|Crook|56011|M|ne|44.7865|-104.1802
WY|071|UNR|Northeastern Crook|WY071|Crook|56011|M|ne|44.8506|-104.1767
AZ|001|VEF|Northwest Plateau|AZ001|Mohave|04015|m|nw|36.5921|-113.3317
AZ|002|VEF|Lake Havasu and Fort Mohave|AZ002|Mohave|04015|m|nw|34.6762|-114.3492
AZ|003|VEF|Northwest Deserts|AZ003|Mohave|04015|m|nw|35.1839|-113.848
AZ|036|VEF|Lake Mead National Recreation Area|AZ036|Mohave|04015|m|nw|35.8011|-114.3194
CA|519|VEF|Eastern Sierra Slopes of Inyo County|CA519|Inyo|06027|P|ee|36.8269|-118.341
CA|520|VEF|Owens Valley|CA520|Inyo|06027|P|ee|36.5133|-118.0127
CA|521|VEF|White Mountains of Inyo County|CA521|Inyo|06027|P|ee|37.0104|-118.0388
CA|522|VEF|Death Valley National Park|CA522|Inyo|06027|P|ee|36.4199|-117.1006
CA|523|VEF|Western Mojave Desert|CA523|San Bernardino|06071|P|ss|35.3053|-117.0005
CA|524|VEF|Eastern Mojave Desert Including the Mojave National Preserve|CA524|San Bernardino|06071|P||35.1398|-115.7069
CA|525|VEF|Morongo Basin|CA525|San Bernardino|06071|P|ss|34.3424|-116.0947
CA|526|VEF|Cadiz Basin|CA526|San Bernardino|06071|P|ss|34.3849|-115.0956
CA|527|VEF|San Bernadino County-Upper Colorado River Valley|CA527|San Bernardino|06071|P|ss|34.4988|-114.5011
NV|014|VEF|Esmeralda and Central Nye County|NV014|Esmeralda|32009|P|sc|37.5763|-116.9511
NV|014|VEF|Esmeralda and Central Nye County|NV014|Nye|32023|P|sc|37.5763|-116.9511
NV|015|VEF|Lincoln County|NV015|Lincoln|32017|P|sc|37.6576|-114.8708
NV|016|VEF|Northeast Clark County|NV016|Clark|32003|P|ss|36.5977|-114.5107
NV|017|VEF|Western Clark and Southern Nye County|NV017|Clark|32003|P|ss|36.5162|-115.9843
NV|017|VEF|Western Clark and Southern Nye County|NV017|Nye|32023|P|sc|36.5162|-115.9843
NV|018|VEF|Sheep Range|NV018|Clark|32003|P|ss|36.7786|-115.1511
NV|018|VEF|Sheep Range|NV018|Lincoln|32017|P|sc|36.7786|-115.1511
NV|019|VEF|Spring Mountains-Red Rock Canyon|NV019|Clark|32003|P|ss|36.2348|-115.6791
NV|019|VEF|Spring Mountains-Red Rock Canyon|NV019|Nye|32023|P|sc|36.2348|-115.6791
NV|020|VEF|Las Vegas Valley|NV020|Clark|32003|P|ss|36.1435|-115.1712
NV|021|VEF|Lake Mead National Recreation Area|NV021|Clark|32003|P|ss|35.9412|-114.5934
NV|022|VEF|Southern Clark County|NV022|Clark|32003|P|ss|35.5358|-115.0222
FL|322|JAX|Northern Columbia|FL322|Columbia|12023|E|nn|30.4143|-82.5870
FL|422|JAX|Southeastern Columbia|FL422|Columbia|12023|E|nn|30.1473|-82.5731
FL|522|JAX|Southwestern Columbia|FL522|Columbia|12023|E|nn|30.0264|-82.7012
OR|101|PQR|Clatsop County Coast|OR101|Clatsop|41007|P|nw|46.0848|-123.8453
OR|102|PQR|Tillamook County Coast|OR102|Tillamook|41057|P|nw|45.3813|-123.8935
OR|103|PQR|Central Coast of Oregon|OR103|Lincoln|41041|P|wc|44.5185|-124.0171
OR|103|PQR|Central Coast of Oregon|OR103|Lane|41039|P|wc|44.5185|-124.0171
OR|104|PQR|North Oregon Coast Range Lowlands|OR104|Tillamook|41057|P|nw|45.7917|-123.4834
OR|104|PQR|North Oregon Coast Range Lowlands|OR104|Clatsop|41007|P|nw|45.7917|-123.4834
OR|104|PQR|North Oregon Coast Range Lowlands|OR104|Lincoln|41041|P|nw|45.7917|-123.4834
OR|104|PQR|North Oregon Coast Range Lowlands|OR104|Washington|41067|P|nw|45.7917|-123.4834
OR|104|PQR|North Oregon Coast Range Lowlands|OR104|Yamhill|41071|P|nw|45.7917|-123.4834
OR|105|PQR|Central Oregon Coast Range Lowlands|OR105|Lane|41039|P|wc|44.3784|-123.7351
OR|105|PQR|Central Oregon Coast Range Lowlands|OR105|Lincoln|41041|P|wc|44.3784|-123.7351
OR|105|PQR|Central Oregon Coast Range Lowlands|OR105|Benton|41003|P|wc|44.3784|-123.7351
OR|105|PQR|Central Oregon Coast Range Lowlands|OR105|Polk|41053|P|wc|44.3784|-123.7351
OR|106|PQR|North Oregon Coast Range|OR106|Tillamook|41057|P|nw|45.6454|-123.4735
OR|106|PQR|North Oregon Coast Range|OR106|Clatsop|41007|P|nw|45.6454|-123.4735
OR|106|PQR|North Oregon Coast Range|OR106|Columbia|41009|P|nw|45.6454|-123.4735
OR|106|PQR|North Oregon Coast Range|OR106|Washington|41067|P|nw|45.6454|-123.4735
OR|106|PQR|North Oregon Coast Range|OR106|Yamhill|41071|P|nw|45.6454|-123.4735
OR|107|PQR|Central Oregon Coast Range|OR107|Lane|41039|P|wc|44.4253|-123.6254
OR|107|PQR|Central Oregon Coast Range|OR107|Lincoln|41041|P|wc|44.4253|-123.6254
OR|107|PQR|Central Oregon Coast Range|OR107|Benton|41003|P|wc|44.4253|-123.6254
OR|107|PQR|Central Oregon Coast Range|OR107|Polk|41053|P|wc|44.4253|-123.6254
OR|108|PQR|Lower Columbia River|OR108|Columbia|41009|P|nw|45.9591|-122.9767
OR|109|PQR|Tualatin Valley|OR109|Washington|41067|P|nw|45.5144|-123.0010
OR|109|PQR|Tualatin Valley|OR109|Multnomah|41051|P|nw|45.5144|-123.0010
OR|109|PQR|Tualatin Valley|OR109|Clackamas|41005|P|nw|45.5144|-123.0010
OR|110|PQR|West Hills and Chehalem Mountains|OR110|Washington|41067|P|nw|45.4599|-122.9062
OR|110|PQR|West Hills and Chehalem Mountains|OR110|Multnomah|41051|P|nw|45.4599|-122.9062
OR|110|PQR|West Hills and Chehalem Mountains|OR110|Yamhill|41071|P|nw|45.4599|-122.9062
OR|111|PQR|Inner Portland Metro|OR111|Multnomah|41051|P|nw|45.4718|-122.6157
OR|111|PQR|Inner Portland Metro|OR111|Clackamas|41005|P|nw|45.4718|-122.6157
OR|112|PQR|East Portland Metro|OR112|Multnomah|41051|P|nw|45.5186|-122.4069
OR|113|PQR|Outer Southeast Portland Metro|OR113|Multnomah|41051|P|nw|45.3705|-122.3697
OR|113|PQR|Outer Southeast Portland Metro|OR113|Clackamas|41005|P|nw|45.3705|-122.3697
OR|114|PQR|West Central Willamette Valley|OR114|Yamhill|41071|P|nw|45.0867|-123.2391
OR|114|PQR|West Central Willamette Valley|OR114|Polk|41053|P|nw|45.0867|-123.2391
OR|115|PQR|East Central Willamette Valley|OR115|Marion|41047|P|nw|45.0421|-122.8253
OR|115|PQR|East Central Willamette Valley|OR115|Clackamas|41005|P|nw|45.0421|-122.8253
OR|116|PQR|Benton County Lowlands|OR116|Benton|41003|P|wc|44.4987|-123.3084
OR|117|PQR|Linn County Lowlands|OR117|Linn|41043|P|wc|44.5207|-122.9602
OR|118|PQR|Lane County Lowlands|OR118|Lane|41039|P|wc|44.0605|-123.1621
OR|119|PQR|West Columbia River Gorge of Oregon above 500 ft|OR119|Multnomah|41051|P|nw|45.5420|-122.0850
OR|119|PQR|West Columbia River Gorge of Oregon above 500 ft|OR119|Hood River|41027|P|nw|45.5420|-122.0850
OR|120|PQR|West Columbia River Gorge I-84 Corridor|OR120|Multnomah|41051|P|nw|45.6063|-122.0573
OR|120|PQR|West Columbia River Gorge I-84 Corridor|OR120|Hood River|41027|P|nw|45.6063|-122.0573
OR|121|PQR|Upper Hood River Valley|OR121|Hood River|41027|P|nw|45.6055|-121.5868
OR|122|PQR|Central Columbia River Gorge I-84 Corridor|OR122|Hood River|41027|P|nw|45.7005|-121.6071
OR|123|PQR|Clackamas County Cascade Foothills|OR123|Clackamas|41005|P|nw|45.2088|-122.2583
OR|124|PQR|Cascade Foothills of Marion and Linn Counties|OR124|Marion|41047|P|wc|44.5450|-122.5773
OR|124|PQR|Cascade Foothills of Marion and Linn Counties|OR124|Linn|41043|P|wc|44.5450|-122.5773
OR|125|PQR|Lane County Cascade Foothills|OR125|Lane|41039|P|wc|43.9499|-122.7232
OR|126|PQR|North Oregon Cascades|OR126|Clackamas|41005|P|nw|45.2324|-121.9183
OR|126|PQR|North Oregon Cascades|OR126|Hood River|41027|P|nw|45.2324|-121.9183
OR|126|PQR|North Oregon Cascades|OR126|Multnomah|41051|P|nw|45.2324|-121.9183
OR|127|PQR|Cascades of Marion and Linn Counties|OR127|Marion|41047|P|wc|44.5856|-122.1211
OR|127|PQR|Cascades of Marion and Linn Counties|OR127|Linn|41043|P|wc|44.5856|-122.1211
OR|128|PQR|Cascades of Lane County|OR128|Lane|41039|P|wc|43.8198|-122.2756
WA|201|PQR|South Washington Coast|WA201|Pacific|53049|P|sw|46.5078|-123.9011
WA|202|PQR|Willapa and Wahkiakum Lowlands|WA202|Pacific|53049|P|sw|46.4823|-123.5766
WA|202|PQR|Willapa and Wahkiakum Lowlands|WA202|Wahkiakum|53069|P|sw|46.4823|-123.5766
WA|203|PQR|Willapa Hills|WA203|Pacific|53049|P|sw|46.4636|-123.4406
WA|203|PQR|Willapa Hills|WA203|Wahkiakum|53069|P|sw|46.4636|-123.4406
WA|203|PQR|Willapa Hills|WA203|Cowlitz|53015|P|sw|46.4636|-123.4406
WA|204|PQR|Cowlitz County Lowlands|WA204|Cowlitz|53015|P|sw|46.1895|-122.9135
WA|205|PQR|North Clark County Lowlands|WA205|Clark|53011|P|sw|45.7787|-122.6057
WA|206|PQR|Inner Vancouver Metro|WA206|Clark|53011|P|sw|45.6678|-122.6462
WA|207|PQR|East Clark County Lowlands|WA207|Clark|53011|P|sw|45.6042|-122.3953
WA|208|PQR|South Washington Cascade Foothills|WA208|Clark|53011|P|sw|46.0337|-122.5546
WA|208|PQR|South Washington Cascade Foothills|WA208|Cowlitz|53015|P|sw|46.0337|-122.5546
WA|208|PQR|South Washington Cascade Foothills|WA208|Skamania|53059|P|sw|46.0337|-122.5546
WA|209|PQR|West Columbia River Gorge - SR 14|WA209|Skamania|53059|P|sw|45.6379|-122.0056
WA|210|PQR|Central Columbia River Gorge - SR 14|WA210|Skamania|53059|P|sw|45.7152|-121.7109
WA|211|PQR|South Washington Cascades|WA211|Skamania|53059|P|sw|46.0559|-122.0135
WA|211|PQR|South Washington Cascades|WA211|Cowlitz|53015|P|sw|46.0559|-122.0135
WA|211|PQR|South Washington Cascades|WA211|Clark|53011|P|sw|46.0559|-122.0135
"""

def extract_number(entry):
    parts = entry.split('|')
    return int(parts[1])

def filter_by_state(data, state_code):
    if state_code:
        return [entry for entry in data if entry.startswith(state_code)]
    return data

def main(state_code=None):
    global data
    # Convert the multiline string to a list of strings, removing any empty lines
    data = [line.strip() for line in data.split('\n') if line.strip()]
    
    if not data:
        print("Error: The data list is empty. Please populate it with entries.")
        return
    
    if not state_code:
        state_code = input("Please enter two character state code or leave blank to do all states: ").strip().upper()
    
    filtered_data = filter_by_state(data, state_code)
    sorted_data = sorted(filtered_data, key=extract_number)
    
    # Write the sorted data to 'sorted_codes' file
    with open('sorted_codes', 'w') as output_file:
        for entry in sorted_data:
            output_file.write(entry + '\n')
    
    print("Sorted data has been written to 'sorted_codes'.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()