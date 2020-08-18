import webbrowser

post_url = input("Enter post url: ")
download_url = "savefrom.net/"+post_url     #Redirects to the website "savefrom.net" where we can easily download posts by pasting url

webbrowser.open(download_url)