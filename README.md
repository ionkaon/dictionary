# 甬江話字詞表

本倉庫包含五份甬江小片方言的同音字表及一份甬江小片方言的詞表，均爲 TSV（製表符分隔）格式。所有的註音均使用吳語學堂式吳拼。

## 字表

文件 [`字表.tsv`](字表.tsv) 是完整的字表，爲了製作 [寧波話吳語拼音輸入方案](https://github.com/NGLI/rime-wugniu_gninpou) 而作。該字表現階段包含寧波（老三區）、鎮海、北侖、舟山定海四個地方的口音。後續可能會加入更多甬江小片各地的口音作爲對照。在文件夾 [`各地字表`](各地字表) 中，也有單獨存放的各地字表。

## 詞表

文件 [`詞表.tsv`](詞表.tsv) 是詞表，同樣是爲了製作 [寧波話吳語拼音輸入方案](https://github.com/NGLI/rime-wugniu_gninpou) 而整理。詞表中包含多部辭書的詞彙，包括湯版《寧波方言詞典》、《阿拉宁波话(修订版)》、朱版《宁波方言词典》、《活色生香宁波话》等。除此以外，詞表中還包含了個人整理的許多詞彙和短語。對於前三本辭書中已收錄的詞，詞表中標出了該詞在辭書中頁碼以便使用者查詢。在此也徵集更多寧波話詞彙。如有詞表未收的寧波話詞彙，歡迎通過 [反饋](https://github.com/ionkaon/dictionary#反饋) 裏的方式聯繫我，告訴我讀音和釋義。詞表將持續更新。

## 音系與拼音方案

見 [音系與拼音方案](音系與拼音方案.md)。

## 字表說明

1. 字表提供的讀音在「兼容格式」一欄，並非純粹的吳拼，具體請參照 [兼容格式](https://github.com/ionkaon/dictionary#兼容格式) 一節。
2. 老三區讀音參照了多本資料，對於同一個字的單字調，幾種資料有時會有出入，此時以湯版《寧波方言詞典》的記錄爲準。
3. 對於老三區口音，若某字在資料中的兩個讀音符合吳拼教程 [新老差異](https://ionkaon.github.io/phin-in-tutorial/内部差异/新老差异.html) 一節中提到的第 3 點到第 12 點。字表內只記錄其中的老派讀音。
4. 寧波（老三區）老派口音僅有 7 個單字調，其中陽上併入了陽去。但在兩字組的前字位置，陽上陽去有所不同。陽上變爲 23，陽去變爲 22。字表中依據變調的不同將兩者分別標爲 4 和 6。注意這 **並不** 表示兩者的單字調有區別。對於單字調爲陽上陽去，且不出現在前字位置的那些字，字表中依照該字在中古的調類標註。這可能會導致一些錯誤，請使用者自行考量。
5. 每個字的字音所參考的資料標註在「出處」一欄。數字表示後面所列的 11 種 [參考資料](https://github.com/ionkaon/dictionary#參考資料) 的編號。例如出處爲 1，則表示該字的字音來源於湯版《寧波方言詞典》。
6. 參考資料 6. 《鄞縣通志》和 7. 《The Ningpo Syllabary》記錄的是古寧波話。兩者的音系和現在的寧波話有不少差別。所以字表「出處」一欄標註爲 6 和 7 的字，讀音經過了推導。其中《The Ningpo Syllabary》原書不標註聲調，字表中的聲調參照中古的調類標註。無論字音的推導還是聲調的推導都可能存在錯誤，得到的讀音可能與時音不同。故若得到的字音與前 5 種資料有衝突，字表中將不記錄推導得到的讀音。但許多字不見於前 5 種資料，字表中便會記錄推導得到的讀音，對於這些字音的可信度，請使用者自行考量。
7. 一些字有舊讀和新讀，如「遲」舊讀 ji2，新讀 dzy2，「家」舊文讀 cio1，文讀 cia1。這類字，《The Ningpo Syllabary》中只有舊讀，字表中依照規律收錄了新讀，「出處」標記爲 0。當然，若在前5種資料中就有記錄新舊讀的，則依照前5種資料記錄。
8. 還有一少部分常見字不見於所有 7 種資料，字表中依照中古音推導得到現代音。另有一些新造的化學用字，字表依照讀半邊（如「氫」）或反切（如「羥」）的原則給這些字注音。這些字的「出處」一欄沒有標註，無法保證字音的可信度，使用者在採信時請仔細考慮。
9. 「清末」一欄標註的是《The Ningpo Syllabary》中記錄的字音。「字頻」一欄標註的是 [寧波話輸入法](https://github.com/NGLI/rime-wugniu_gninpou) 中使用的字頻。
10. 一些資料中出現的讀音，個人認爲有錯誤或不合適的，會在「篩選」一欄打上#號。這些讀音將不會出現在輸入法中。

## 詞表說明

1. 詞表提供的讀音在「兼容格式」一欄，並非純粹的吳拼，具體請參照 [兼容格式](https://github.com/ionkaon/dictionary#兼容格式) 一節。
2. 詞表中的讀音爲老派的老三區口音，與字表相同。原辭書中的記音可能並非基於老派音系，在整理成詞表時都推導到了老派音系。
3. 詞表中的寫法經過個人考證，部分詞彙的寫法可能與辭書中的有出入。
4. 限於個人精力，在未來很長一段時間內，絕大部分詞彙都不會有釋義和例句。請讀者根據頁碼自行查閱辭書。

## 兼容格式

輸入法提供老三區和鄞州（鍾公廟、首南附近）兩種口音。爲了兼容鄞州口音，在註音時做了一些設置。一些字會標註兩個吳拼，兩個吳拼用橫槓 - 連接。橫槓前的是城區讀法，後面是鄞州的讀法。例如「安」字，老三區讀音爲 ei1，鄞州讀 e1，在表中「安」就標註爲 ei-e1。老三區的有些讀音在鄞州找不到對應，就在這些吳拼後加橫槓。如「漢」字在老三區有 he5 和 hei5 兩個讀音，在鄞州僅 he5 一音，詞表中就標註 he5 和 hei-5。兩地的讀音差異見輸入法文檔的 [鄞州（钟公庙、首南附近）](https://github.com/NGLI/rime-wugniu_gninpou/wiki/音系及拼音方案#鄞州（钟公庙、首南附近）) 一節。如果僅需要老三區口音，忽略橫槓後的讀音即可。需要注意的是，如果是整個韻的區別，則不做設置。例如老三區老派的 iun 韻母，在鄞州整體併入了 ion 韻母，這類情形就沒有標記，仍舊標爲 iun。

## 精簡版

對於老三區口音，上文 [說明](https://github.com/ionkaon/dictionary#說明) 中第 3 條以及第 5 - 10 條提到，[`字表.tsv`](字表.tsv) 有諸多超出方言志和方言詞典的內容。如果使用者不需要這些內容，也可以查看 [`各地字表`](各地字表) 文件夾下的文件 [`甬城.tsv`](各地字表/甬城.tsv)。精簡版字表只收錄來自前 5 種 [參考資料](https://github.com/ionkaon/dictionary#參考資料) 的字音，不區分陽上和陽去，也沒有爲兼容其他口音而進行改動，更接近原始的參考資料。同時，pure 版字表也不提供字頻等用於輸入法的信息，僅僅提供繁體、简体、吳拼、出處和備註這五列信息。[吳語學堂](https://www.wugniu.com/) 中寧波話字音查詢的數據源便是這張表，網站上的查詢結果僅僅是在本表的基礎上加上了 IPA 一欄，刪去了出處一欄。

## 反饋

限於本人水平，難免會有錯漏。如果使用者有任何問題或是發現了任何錯誤，歡迎提交 [issue](https://github.com/ionkaon/dictionary/issues)，或是通過以下郵箱直接與我聯繫。

本人郵箱：shinzoqchiuq@outlook.com

## 致謝（排名不分先後）

- [曹潔萍](https://www.zhihu.com/people/cao-jie-ping-86)
- [fededem](https://github.com/fededem)
- [Hideyoshi](https://www.zhihu.com/people/jiang-kai-wen-21)
- [Joynese Fu](https://www.zhihu.com/people/joynese-fu)
- [五月_starrysky](https://weibo.com/ngyuq)
- [PeiTsengtung](https://github.com/PeiTsengtung)
- [sacheong](https://github.com/sacheong)
- slim
- [再言](https://www.zhihu.com/people/zai-yan-50)
- [神死慟瞑](https://www.zhihu.com/people/cao-wei-feng)

## 參考資料

1. 湯珍珠、陳忠敏、吳新賢：《寧波方言詞典》，江蘇教育出版社，1997
2. 宁波市地方志编纂委员会：《宁波市志·方言》，中华书局，1995
3. 朱彰年、薛恭穆、周志锋、汪维辉：《阿拉宁波话(修订版)》，宁波出版社，2016
4. 朱彰年、薛恭穆、周志锋、汪维辉：《宁波方言词典》，汉语大辞典出版社，1996
5. 周志锋：《江苏教育版<宁波方言词典>词目用字问题》，方言 2008 年第一期
6. 《鄞縣通志·文獻志·方言》，鄞縣通志館，1951
7. P. G. von Möllendorff：《The Ningpo Syllabary》，Shanghai: American Presbyterian Mission Press，1901
8. 陈忠敏：《鄞县方言同音字汇》，方言 1990 年第一期
9. 《镇海县志》编纂委员会：《镇海县志·方言》，中国大百科全书出版社上海分社，1994
10. 周志锋、胡方：《北仑方言》，中国文史出版社，2007
11. 方松熹：《舟山方言研究》，社会科学文献出版社，1993
12. 岱山县志编纂委员会：《岱山县志·方言》，浙江人民出版社，2006
12. 周时奋：《活色生香宁波话》，宁波出版社，2000

