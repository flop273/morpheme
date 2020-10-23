from janome.tokenizer import Tokenizer

# 外部ファイルの読み込み
fp=open("./test.txt", "rt", encoding='utf-8')
text=fp.read()

# Janomeの準備
tok = Tokenizer()
# tokens = tok.tokenize("智に働けば角が立つ。")
tokens = tok.tokenize(text)

# 形態素をカウント
counter={}
for t in tokens:
    bf=t.base_form
    if not bf in counter:
        counter[bf]=0
    counter[bf]+=1
    # print(t)

# カウントの多い順に並び替え
sc= sorted(counter.items(), key=lambda x: x[1], reverse=True)
# 表示
for i, t, in enumerate(sc):
    if i >=100:
        break
    key, cnt=t
    print((i+1), ".", key, "=", cnt)