# Beauty-and-Best
INF 551 final project, IoT



In the world of Internet, people would like to connect things in their life to make their life easier. From the most basic rice cooker to the Iron Man style personal assistance Jarvis. The concept of IoT is identical which is to collect user data and allow them to operate different things with internet. For this class, we are studying database, how to manage cloud database and other concepts such as API. For our final project, we somehow need to use dataset management to record data, share data and make a product out of user data.

The idea of Beauty and Best is about recording people’s daily data to monitor people’s habit and give user suggestions. From my personal experience, I spend too much time for doing my makeup while watching tv shows or series. At the beginning, I feel that using voice command might be a good fit for this product. However, this also brings more problem of voice recognition and machine translation. Since there are many TV shows are not in English which might have different names and different accesses. Therefore, I just use text to make records for gathering data. For this time, I use an IOS App to record my daily watching and dressing activities, also this app could generate suggestions about dress and shows for me based on my history. Other than that, I also add another feature to this application which is allowing people to write diary on this app and do sentiment analysis to those words. If the analysis score is high on negative which triggers the threshold, then the system will generate a text message and send it out to your friend. 

There are few hard wares that I need to use design this project, even though some of them are not easy to get. However, they could definitely work as the way I wished. The magic mirror from Microsoft which could be the main display and interactive panel for users. The echo or any kinds of smart home devices could be my input sources. Now I am using an iPhone as my input source. After we have the data, the intelligent recommendation dress system and video suggestion system would give me the suggestion based on my needs and preference which will be programmed by me in python. For software wise, I use python to create the basic recommendation system and record the data. I also designed the user interface with sketch and make it alive with Xcode using swift. Even though I do have some difficulties with using python codes with Xcode to link them with the real App. Therefore, I use Kivy which is a python library for designing App. 

Before introducing the design, I would like to say how I record the data and manage them with firebase. I use JSON to record my data. There are four categories of data that I would like to keep track with. Such as the date, the dress, video type and video name. During this period, I recorded from January 14th to March 28th. I summarized my dressing styles into four categories, sports, casual, dress and business. Even though, I never wear any business style clothes during this period. In this period, I mainly watched Super Vocal, HIMYM, Office, Unnatural. The Super Vocal is approximately 90 to 110 minutes per episode, other than that, TV series are 30 to 40 minutes per episode. So, the time is various when we detect the type and length of video. During my suggestion system, I would recommend the user to finish their leftovers when they ask for recommendations. If they do not want our recommendations, they could also type their desire shows by hands.

![firebase JSON](/final_report/firebase.png)

Figure 1. Firebase JSON file

For the cloth recommendation system, I have a simple philosophy which is not wearing the same style as yesterday. So, if I wear casual cloth yesterday, I would like to wear some sports today. Other than that, I do have some days that I want to wear the same style, or I want the system to surprise me. 

After I gather those data, I use JSON in python to read and load them into a dictionary which will would provide me a clean key-value pair form which is easily navigable. Then, I use firebase to store and manage keep data and make suggestions from the online data. Every time I update data, the program will erase the old version of JSON and replace it with a newer version. Additionally, another program which uses sentiment analysis API to analysis personal diary which would decide sent a text message to target cell phone or not.

Now I would like to introduce my IOS App interface made by both Xcode and Kivy. For the Xcode version, I make a splash page with my icon and this page will disappear in several seconds. Then the main page shows login username and passwords. After we log into the app, there are three icons representing video, time and diary. When you tap the button, you can get into the specific section and when you tap the back button, you can get back to the menu page. This is a user-friendly interface, however, swift does not compile with python which I develop all of my function with. 

![Xcode interface](/final_report/xcode_interface.png)

Figue2. Xcode designed interface

Therefore, I switch to use a library called Kivy from python which is an object orientated programming package which is also a challenge for me since I have never tried this kind of programming before. For the Kivy version, I design the interface for gathering input such as date and diary from users and update that to the firebase. After that, the program I wrote for functions will generate the recommendations and decide to generate the text messages for sending or not.

![kivy interface](/final_report/kivy_interface.png)

Figure 3. Kivy interface

For the suggestion of dresses and video for users, I use the data to generate user’s habit and make random suggestions for users. Additional to that, I will suggest the user to finish their leftovers when the last video was not finished by the user. For the dress suggestion, I make sure that user should not wear the same type of outfit every day. Then the suggestion will be updated to the firebase when we give the new date which is not included in the earlier version. Since I use date as the key for the JSON file, which python could look through the file and make sure the user is not changing the history.

![result 1](/final_report/result_1.png)

![result 2](/final_report/result_2.png)

Figure 4-5, results of suggestions for a new date, Mar 30th

For the sentiment Analysis part, I use two sentiment analysis tools. The first one is an API called Watson from IBM which will detect tone of each sentence of a paragraph. Watson will categories each sentence into a tone such as Sadness, Joy, Analytical and provide a confidence score for this sentence. The second method is a python library called blob which will classify the sentence as positive or negative and also provide a confidence score for the sentence. I use both of those analytical tools to get the dominate mood and confidence score. First of all, I collect the tone for each sentence in the target paragraph and pick the most frequent mood as the dominate mood. Then, I assign some of those tones as negative, such as Sadness, Angry and calculate the average confidence score along with the score from the blob result. 

Other than using well-developed API from other developers, I also introduce some red flag system which will add a weight to the confidence score which will trigger the sending function to send message through texts. The red flag system contains several words that we consider as red flags such as “kill”, “suicide” and other dangerous words. After we get the weighted confidence score, there is another API called Twilio will send text messages to user’s friend and ask for help. Users could choose to mute this function if they decide to keep it down, however, the purpose for my App is to help user to reach out when they want but they could not do this by themselves.

![text](/final_report/text.jpg)

Figure 6. message sent when the diary is very negative

Unlike my counterparts, I do this project by myself which brings me both challenges and special experiences in many aspects such as coding, time management, user experience research, learning by doing, etc. I have been learning a lot since I have to force myself to think like a group and also being so self-discipline to work. In the future, I could do better for sticking on my time schedule and learn more about objective orientated programming and swift since they are very useful and powerful since we all want to make our idea come true rather than have sketches with no functions.



