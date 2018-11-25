import pyexcel

#2 prepare
list=[
    {"name":"n",
    "age":5,

    },
    {
        "name":"a",
        "age":6,
    }
    ]
#save as
pyexcel.save_as(records=list,dest_file_name="helo.xlsx")