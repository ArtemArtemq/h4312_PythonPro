import requests

res_parse_dict = {}
res_parse_list = []
res_parse_list_2 = []

response = requests.get("https://coinmarketcap.com/")
response_text = response.text
response_parse = response_text.split("<span>")
response_parse_names = response_text.split('coin-item-name')

for parse_name_1 in response_parse_names:
    if parse_name_1.startswith('">'):
        for parse_name_2 in parse_name_1.split("</p>"):
            if parse_name_2.startswith('">'):
                res_parse_list_2.append(parse_name_2[2:])

for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("$"):
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                res_parse_list.append(parse_elem_2)

for i in range(len(res_parse_list_2)):
    res_parse_dict[f"{res_parse_list_2[i]}"] = f"{res_parse_list[i]}"

print(res_parse_dict["XRP"])