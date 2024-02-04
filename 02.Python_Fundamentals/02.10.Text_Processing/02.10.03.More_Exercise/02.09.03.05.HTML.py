title = input()
content = input()
command = input()
comments = []

while command != "end of comments":
    comments.append(command)

    command = input()


print(f"<h1>\n    {title}\n</h1>")
print(f"<article>\n    {content}\n</article>")
for comment in comments:
    print(f"<div>\n    {comment}\n</div>")
