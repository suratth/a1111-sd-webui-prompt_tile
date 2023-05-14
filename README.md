# a1111-sd-webui-prompt_tile
Extension to manage prompts with GUI on WebUI

#Hello!
This extension is created by modifying the following extension.
https://github.com/KohakuBlueleaf/a1111-sd-webui-lycoris

Instead of supporting lycoris, it displays a .txt file with a prompt description as a card.

Let's manage Styles.csv with GUI! is the purpose.

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
