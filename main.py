meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное"
            }
word = input("Введите непонятное слово (большими буквами!): ")


if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('У нас нет такого слова, Но мы над этим работаем')
            
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('У нас нет такого слова, Но мы над этим работаем')
            
meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное"
            }
word = input("Введите непонятное слово (большими буквами!): ")


if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('У нас нет такого слова, Но мы над этим работаем')
            
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('У нас нет такого слова, Но мы над этим работаем')

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))
            
