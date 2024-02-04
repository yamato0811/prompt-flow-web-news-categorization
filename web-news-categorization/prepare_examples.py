from promptflow import tool


@tool
def prepare_examples():
    return [
        {
            "url": "https://news.yahoo.co.jp/pickup/6490497",
            "text_content": "関東地方では明日から大雪の恐れがあり、東京23区でも積雪の可能性がある。朝は日差しが出るが、夜には雪が降るため、ノーマルタイヤでは危険であり、冬装備が必要とされている。",
            "category": "国内",
            "reason": "国内天気のトピックのため",
        },
        {
            "url": "https://news.yahoo.co.jp/articles/ddfaff939ee49a2e084ccaa85d2d75f92ab17aa8",
            "text_content": "ジョー・バイデン大統領が南部サウスカロライナ州予備選で圧勝し、再選を目指す意向を示した。バイデン氏は黒人層の支持を固めるために同州の黒人教会を訪れ、黒人票で再び圧倒する戦略が求められるとされている。",
            "category": "国際",
            "reason": "アメリカの政治トピックため",
        },
        {
            "url": "https://news.yahoo.co.jp/articles/618c34d325febd83959a3a51a50292b676fa7f6e",
            "text_content": "東京都内の住宅地では、私鉄の沿線ごとにライフスタイルが異なる。東急電鉄の沿線は大卒者が多く、教育機関も充実している。しかし、世代を追うごとにそのほかの地域との格差が開いている。",
            "category": "経済",
            "reason": "住宅地に関するトピックため",
        },
        {
            "url": "https://news.yahoo.co.jp/articles/be17e44b68ad2dda4c34056a9f821928ca4a8790",
            "text_content": "俳優の宮世琉弥が20歳の誕生日に家族と乾杯し、20代での目標を明かした。また、彼のカレンダーの撮影は地元の仙台で行われ、自然体で柔和な姿やクールでスタイリッシュな佇まいが堪能できる。",
            "category": "エンタメ",
            "reason": "俳優のトピックため",
        },
        {
            "url": "https://news.yahoo.co.jp/articles/be17e44b68ad2dda4c34056a9f821928ca4a8790",
            "text_content": "日本ハムの有薗直輝が紅白戦でホームランを放ち、同期の選手たちも期待されている。",
            "category": "スポーツ",
            "reason": "プロ野球のトピックため",
        },
        {
            "url": "https://news.yahoo.co.jp/articles/7ee3f6c46f66673871ac161517f252c7e3b51371",
            "text_content": "ドイツの哲学者マルクス・ガブリエル氏は、AIの悪用による危機を指摘している。生成AIを用いたフェイク情報の拡散や、AIが正しいという思い込みによる誤った回答などが問題とされている。",
            "category": "IT",
            "reason": "AIのトピックため",
        },
        {
            "url": "https://news.yahoo.co.jp/articles/622a6737fbe81ea35d1bead944c1b5f3032ffe2e",
            "text_content": "2月2日夜、直径約290mの小惑星が地球付近を通過する。NASAは監視中であり、危険はないと発表している。",
            "category": "科学",
            "reason": "小惑星のトピックため",
        },
        {
            "url": "https://news.yahoo.co.jp/articles/2e5e946bb2e3f51d026ae6f5cdedb51e0150f2de",
            "text_content": "There is no content available for this text.",
            "category": "None",
            "reason": "None",
        },
    ]
