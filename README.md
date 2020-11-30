# Gamerbase

The initial thought of this site came from the project ideas. I'd looked over the 
ideas and I come across the one where people could upload their own reciepes, and 
the site publisher would be able to link in, the appropriate kitchen appliance to use.
Then it got me thinking, about gaming, it's a big community out there, in which more
and more people are joining into it each day!


So, my idea was to create a database, where people could upload, their honest reviews,
about the game that they've been playing, including on which platform they've been playing
it on (Xbox One, Playstation 4, etc) and then each review, would have a link under it,
where the person reading, could purchase the game if they wanted. So it would essentially 
be an online shop, that'd solely rely on gamers reviews of the game.

## UX
This website is for people of the gaming community, which in this day and age, theres Millions of people playing online, and from what I've found
games always sell better, from word of mouth, from people actually playing the game and giving their honest opinion on it.
So my idea behind this project, is to build a website, that people would be able to come on, search for a game they've heard about,
read the reviews that have been posted about it, then if they want, they can purchase the game at the same time.

For example, User story guy 29 years old, he plays a lot of games, I mean, he's the kind of guy that is always online, streaming his games to people all over the world.
Now, one question he gets asked all the time, "what do you think to ******". In which, he's constantly hearing it, so he's after somewhere that he can
write his reviews out of a game, and then say to people, I've wrote a review on the game you've asked about, you can read it on here (Gamerbase).

Another user is someone, who likes to play games on his Playstation, but doesn't get to go on it that often, and as we know, the games aren't the cheapest
either! So, he want's to hear about what other people think of the game, before forking out near on £50 for a game, which is smart, because there's a lot of 
games out there that have been hyped up massively, then the game itself just flops. For example, from what I remember, around 90% of the people that bought
the Avengers game, whene it first came out, aren't playing it anymore, the people who made the game, haven't even made their money back from making the game in 
the first place! So for our user here, the Gamerbase site would be perfect, so then he can do his research, see what people genuinly think of the game, before 
potentially wasting his money.



This is How I had initially planned for the page to be laid out

![Base page](/static/images/base-page.png)
1. The search bar in the original idea, was for it to be in the top left corner, with the nav buttons to all be showing in the top left
1. After building the sight and viewing in the mobile view, the search bar just didn't sit right, it was too blocky, whether this was down to my lack of experience or not? But I ended up opting to a style previously shown in the tutorials
1. I also felt, the site itself gives off a neater feel, with the majority of the Nav bar buttons, hidden away in a menu, that pops up from the left hand side when required.

This with the review sections visible

![Base page with review](/static/images/base-page-with-review-open.png)

These are the log in / Register Pages

![Register page](/static/images/register.png)

![Log in page](/static/images/log-in.png)


## Features
### Feature 1 on the home page
It allows people to come onto the site and read reviews by simply clicking on the header. The feature in this feature, is that it 
contains a search bar, allowing users to search for a game they desire to read someones view on. The search bar is easily found, 
just above the reviews them self, if they have used the search feature and want to return to a full list, they can simply hit the 
Reset button, and it'll do as it says, reset the page.
1. A added feature onto the reviews, on the 'Do I recommend this game?' Each of the different answers have different icons to represent it:
    1.  YES - has smiley face with love hearts in the eyes
    2. NO - has a sad face
    3. You need to play it, to make your own decision has a 'meh' emoji face, essentialy '  :|   '



### Feature 2 
users can register their own account on the site, to do this they: 
1. Click on the menu button in the top left corner
1. then click on Register
1. Once the register page has loaded, the user can then fill out the form, with their desired username and password and click submit
1. Once that's been completed, the user is then logged in and can carry out other features, including 'Add new review' as well as Log out

### Feature 3
If the user has previous registered and needs to log in, they can simply do this by:
1. clicking on the menu in the top left corner
1. then click on Log in.
1. fill out the form and click 'Log in'

### Feature 4
Once logged in, the user can add their own review to the database by:
1. clicking on the menu button in the top left corner
2. Then clicking on 'Add new review' 
3. Once they're on this page, they'll see a form that needs filling out, including:
    1. Choose the game title
    1. Write their own review of the game in the next section
    1. Then the user has to select which console they play the game on
    1. And also, the final decision, would they recommend this game to others, in which they have 3 different options, including:
        1. Yes
        1. No
        1. You need to play it, to make your own decision
    1. Once they've filled all the required fields out, they can hit Add my Review, the review will then be submitted to the database

### Feature 5
After the User has submitted their review, they can easily change it, or even delete it if they feel like it, by doing the following:
 (editing review)
1. The user can edit their review by, finding the review they want to change( can use the search bar if necessary )
1. Then, they can click on the 'Edit' button, which is found to the right hand side of the review header
1. Once the edit page has loaded, it'll every input field, that they previously filled when they originally added a new review
1. So all the user needs to do, is make the necessary changes to the review, then click the 'Edit my review' button
    1. Note, if they don't want to carry out any editting to their review, they can easily click the cancel button to cancel the editting
1. Once completed, a message will appear above the form, saying 'Your Review was successfully Edited!'
1. The User can return back to the home page, by clicking the 'Cancel' button.

(Deleting Review)
1. If the user wanted to delete their review, all the have to do, once finding the said review, they just have to click on the button, to the right of the header, next to he edit button.
1. Once clicked, this will permanantly delete their review

### Feature 6
The user can easily log out by:
1. clicking on the menu button in the top left corner
1. Then, down at the bottom of the list, is log out, if they click that, they will be brought back to the home page with a flash message saying "You have been logged out"

### Features I'd wished to have implemented given time and Future features:
1. The Search bar.
    1.  As shown in the wireframe pictures further up, I initially wanted the search bar to be in the top left, ideally Exactly like it shows in the picture, but I just couldn't find a way to implement this into the site, so it would work as nice as the wireframe
2. More pictures, I'd of liked to add more Gaming pictures to the forum, to give it a more friendly gaming theme, I've got some pictures included on the login and register page, but I just didn't have the time to implement it else where
3. Add links to purchase each game, or an option, so the person admitting the review could add a link on where to purchase the game, since it was initially designed to sell the games, then an option so they could actually buy the game from them.
4. Possibly to import a database of game titles from IGN, or similar place, then have the options so people can select the games from that list and then add their review to that.
5. Have a more features on the users profile, so for example, 
    1. other users could see other peoples profiles
    2. show what reviews each user has created
    3. show that user's favourite console (because majorirty of gamers have most, myself I have 2 Xbox one's a Nintendo switch and a gaming laptop)
    4. a Display picture

### Technologies used
To start with, I've used the basic HTML, css to create the foundations of the site and edit it to my design

I've just Javascript and JQuery, to implement things like:
1. The side scrolling nav bar
2. the collapsible reviews
3. the dropdown boxes for the forms
4. tool tip, which shows up a help box on the forms
5. form select
6. validate materialize as the drop down selects on forms, wouldn't validate the same way other form inputs validate
7. also, it allowed us to build a base page, in which all of the other pages extended from it, making it quicker to build pages

Python. Python was used to build the ap itself, to be able to Carry out CRUD with the database and fully work.

### Testing

For testing, I carried out a lot of it myself, clicking on all the links, making sure all of the relevant fields required to be filled out before completion

I also had my friend help me out and try out the website to see if he could find any faults

His username is (grandsnorlax), He's a good friend of mine, and when I originally told him about the project, I shared the link to the Task manager page that we built in the tutorials

Now, when he went onto said site, he went to register, and found an issue straight away, on the register form, we put on that the password would only allow, a-z lowewr and higher case, along with numbers

So, when he tried to register, he had this message:
![Log in fail](/static/images/login-fail.jpg)

Now, Their is no message, to tell users what specific format they can and can't use

![Help sign on register page](/static/images/register-help.jpg)

Learning from this, I added a hover feature next to the username and password labels, so that if they did enter a wrong character, or even not enough or too many characters, they can easily find the relevant information, making it user friendly.




## 

Testing
In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

Deployment
This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

Different values for environment variables (Heroku Config Vars)?
Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.

Credits
Content
The text for section Y was copied from the Wikipedia article Z
Media
The photos used in this site were obtained from ...
Acknowledgements
I received inspiration for this project from X