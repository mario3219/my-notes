**Editing**

| Commands          | Description              |
| ----------------- | ------------------------ |
| u                 | Undo                     |
| Ctrl+r            | Redo                     |
| :%s/\<old\>/new/g | replace text to new text |
| :%s/\Vold/new/g   | with weird unix          |

**Navigation**

| Commands   | Description                  |
| ---------- | ---------------------------- |
| set number | Show line numbers            |
| \<line\>   | Jump to line                 |
| Ctrl+d     | Jump half screen down        |
| Ctrl+u     | Jump half screen up          |
| /\<text\>  | Find text                    |
| n          | Jump to next match           |
| N          | Jump to previous match       |
| :noh       | Clear search highlights      |
| gg         | Jump to beginning of file    |
| G          | Jump to end of file          |
| $          | Jump to end of line          |
| 0          | Jump to beginning of line    |
| e          | Jump one word forwards       |
| b          | Jump one word backwards      |
| Shift+e    | Jump one word forwards fast  |
| Shift+b    | Jump one word backwards fast |


**Visuals**

| Commands | Description          |
| -------- | -------------------- |
| ls       | List unsaved changes |

**Window operations**

| Commands            | Description         |
| ------------------- | ------------------- |
| qa                  | Quit all            |
| qa!                 | Force quit all      |
| enew                | New buffer window   |
| e                   | Refresh             |
| e filename          | Edit file           |
| vsplit              | Vertical split      |
| split               | Horizontal split    |
| botright split      | Create lower window |
| vertical resize +20 | Horizontal resizing |
| resize +20          | Vertical resizing   |
| tabnew              | Create tab          |
| tabclose            | Close tab           |
| tabs                | List tabs           |
| gt                  | Next tab            |
| gT                  | Previous tab        |
| Explore             | Explorer            |

**Other**

| Commands                       | Description                              |
| ------------------------------ | ---------------------------------------- |
| q -> ENTER -> \<key\> -> ENTER | Start recording macro and mapping to key |
| q                              | Stop recording                           |
| @\<key\>                       | Run macro                                |
