# hello!

# english
This extension is created by modifying the following extension.
https://github.com/KohakuBlueleaf/a1111-sd-webui-lycoris

Instead of supporting lycoris, it displays a .txt file with a prompt description as a card.

Let's manage Styles.csv with GUI! is the purpose.
Preview images and prompts (positive/negative) can be managed like Lora.

[How to use]
(1) Create the following directory.
　stable-diffusion-webui\models\PRONPT
(2) Create a .txt that describes the prompt description.
・Set the file name to the display name (prompt description).
・The contents are as follows.
　pro: positive prompt
     neg: negative prompt
③ PRONPT will be displayed in the extra networks function (Hanafuda)!

【Notes】
Some code is hardcoded depending on my path.
・Some functions (such as deletion of prompt) are not yet implemented.
・I made a tool to convert Styles.csv to .txt.
"will be published soon."
・I am a person from a different field who usually develops embedded programs in C language.
Please forgive me if there are any flaws in Git rules, licenses, etc.

There may be various flaws and rule violations.
I will try to respond as much as possible.

# japanese
本拡張機能は、下記拡張機能を改変して作成されています。
https://github.com/KohakuBlueleaf/a1111-sd-webui-lycoris

lycorisをサポートする代わりに、promptの説明を記載した.txtファイルをカードとして表示します。

Styles.csvをGUIで管理しよう！が趣旨です。
プレビュー画像とプロンプト（ポジティブ/ネガティブ）を、Loraのように管理できます。

【使い方】
①下記ディレクトリを作成します。
　stable-diffusion-webui\models\PRONPT
②プロンプトの説明を記載した.txtを作成します。
・ファイル名は表示名（プロンプトの説明）に設定します。
・中身は下記を記載します。
　pro:ポジティブプロンプト
    neg:ネガティブプロンプト
③extra networksの機能（花札）にPRONPTが表示されます！

【注意事項】
・一部のコードは私のパスに依存したハードコーディングです。
・一部の機能（promptの削除など）は未実装です。
・Styles.csvを.txtに転機するツールを作りました。
　そのうち公開します。
・私は普段は組み込みをC言語で開発している畑違いの人間です。
　Gitのルールや、ライセンスなど、不備があればお許しください。

様々な不備やルール違反があるかもしれません。
可能な限り対応しようと思っています。
