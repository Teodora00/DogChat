from datetime import datetime



comment1 = {
    "Text" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "Name": "Charlie",
    "Username" : "chucky",
    "Picture" : "charlie_profile.png",
    "DateTime" : datetime(2021, 7, 1, 18, 0, 0),
}

comment2 = {
    "Text" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "Name": "Melba",
    "Username" : "melba",
    "Picture" : "melba_profile.png",
    "DateTime" : datetime(2021, 7, 1, 18, 30, 0),
}

comment3 = {
    "Text" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "Name": "Melba",
    "Username" : "melba",
    "Picture" : "melba_profile.png",
    "DateTime" : datetime(2021, 6, 29, 9, 30, 0),
}

post1 = {
    "PostId" : 1,
    "Text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "Name": "Melba",
    "Username" : "melba",
    "Likes": ["charlie"],
    "Comments" : [comment1, comment2],
    "DateTime" : datetime(2021, 7, 1, 17, 0, 0),
    "Picture" : "melba_profile.png"
}

post2 = {
    "PostId" : 2,
    "Text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "Name": "Melba",
    "Username" : "melba",
    "Likes": [],
    "Comments" : [],
    "DateTime" : datetime(2021, 6, 30, 12, 30, 0),
    "Picture" : "melba_profile.png"
}

post3 = {
    "PostId" : 3,
    "Text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "Name": "Charlie",
    "Username" : "chucky",
    "Likes": ["melba"],
    "Comments" : [comment3],
    "DateTime" : datetime(2021, 6, 29, 9, 0, 0),
    "Picture" : "charlie_profile.png"
}

test_posts = {
    1 : post1,
    2 : post2,
    3 : post3
}

melba_posts = {
    1 : post1,
    2 : post2
}

charlie_posts = {
    3 : post3
}

charlie = {
    "Name": "Charlie",
    "Bio" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "Username" : "chucky",
    "Picture" : "charlie_profile.png",
    "Birthday" : datetime(2018, 1, 2),
    "Posts" : charlie_posts
}

melba = {
    "Name": "Melba",
    "Bio" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "Username" : "melba",
    "Picture" : "melba_profile.png",
    "Birthday" : datetime(2013, 2, 14),
    "Posts": melba_posts
}

dogs = {
    "melba" : melba,
    "chucky" : charlie
}