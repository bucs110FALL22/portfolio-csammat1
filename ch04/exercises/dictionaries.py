article = 'Hurricane Ian landed in Florida as a dangerous Category 4 hurricane on Thursday. Governor Ron DeSantis and federal authorities have urged residents in the storm’s paths to seek safety by evacuating the area. Some brave souls, however, have decided to weather the storm. Some of them are even getting paid to stand outside and cover the storm’s chaos for the rest of us sitting in our living rooms. That includes Jim Cantore, a legendary reporter for the Weather Channel who has made a career out of reporting from the middle of dangerous storms such as Hurricane Ian. However, the latest hurricane to strike Florida’s coast was almost Cantore’s last. “Jim Cantore almost got struck by lightning,” said Anthony Dominic, adding a Hurricane Ian hashtag. Attempting to throw the broadcast to coverage of the Hurricane’s storm wall in Punta Gana, Florida, Cantor visibly reacted when a thunderous lightning strike hit the immediate area where he was standing. The strike was so close to Cantore’s proximity that the seasoned professional could only shake his head while ending the shot. Thankfully, Cantore appears to avoid any severe injury in the video. Hurricane Ian is expected to batter Florida’s coast into the weekend. Several athletic events have already been moved from the area.The post Hurricane Ian almost kills legendary weatherman appeared first on The Comeback: Today’s Top Sports Stories & Reactions.'


dict = {'hurricane':'big storm',  
'Florida':'the wild south',
'storm':'end of the world',
'weather':'light rain',
'Cantore':'The Legend',
'lightning':"Zue's lightning",}
for (key,value) in dict.items():
  new_string = article.replace(key,value)#not sure why it is not replacing
print(new_string)