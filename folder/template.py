import string

s = """\
    Hi $name

    $contents

    Have a good day    
"""

t = string.Template(s)
ctx = t.substitute(name = "leedonggyu", contents = "my name is leedonggyu")
print(ctx)


## Example
def output_template_file(file_name: str, **kwargs):
    """
        @params:
            name 이름\n
            header 머리\n
            main 몸통\n
            footer 꼬리\n
    """
    with open(file_name, 'r') as f:

        return string.Template(f.read()).substitute(
            name=kwargs["name"],
            header=kwargs["header"],
            main=kwargs["main"],
            footer=kwargs["footer"]
        )

t = output_template_file("public/design.txt",
    name = "leedonggyu",
    header="introduce my self",
    main="my name is leeodnggyu",
    footer="lastly, i work npixel"
)

print(t)
