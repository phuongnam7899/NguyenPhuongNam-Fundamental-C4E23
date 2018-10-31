l_list=[
    {
    "stt":1,
    "ten":"huy",
    "gio lam":30,
    "luong/h":50,
    },
    {
     "stt":2   ,
    "ten":"quan",
    "gio lam":20,
    "luong/h":40,
    },
    {
    "stt":3,
    "ten":"duc",
    "gio lam":15,
    "luong/h":35,
    },
]
sum=0
for l in l_list:
    luong= l["gio lam"]*l["luong/h"]
    print("so gio lam cua ",l["ten"]," la: ",l["gio lam"],"(h)")
    print("luong cua ",l["ten"]," la: ",l["gio lam"]*l["luong/h"],"(nghin dong)")
    sum += luong
print("tong luong la: ",sum,"(nghin dong)")



