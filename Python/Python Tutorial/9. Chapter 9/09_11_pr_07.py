# WAP to find out the line number where python is present or not.

content = True
i = 1
with open("log.txt") as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(content)
            print(f"Yes python is present on line number {i}") 
        i+=1