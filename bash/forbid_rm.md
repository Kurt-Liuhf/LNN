# This note shows a solution to replace `rm` in Linux
The key idea is to build a temporary recycle bin for storing. The trashes will be delete regularly buy configuring the *crontab*.
## 1. Create a recycle bin
- `mkdir path_to_trash/.trash`

## 2. Implement the alternative of `rm`
- `touch trash.sh`:
```
trash_dir="path_to_trash/.trash"
for i in $*; do
    file_stamp=`date +%s`
    file_name=`basename $i`
    mv $1 $trash_dir/$file_name.$file_stamp
```
- `chmod 755 trash.sh`

## 3. Create alias in you *~/.bashrc* or *~/.zshrc*
add the following lines to the *~/.bashrc*
- alias rm='echo "rm is not allow"'
- alias="sh path_to_trash/trash.sh"
put the configurations in force `source ~/.bashrc`


## 4. Set regular deletion
- `crontab -e`
- `0 0 \* \* 0 rm -rf path_to_trash/.trash/*`
Six columns of *crontab*:
<!-- \*           \*              \*           \*             \* -->
<!-- min(0-59)    hours(0-23)     day(1-31)    month(1-12)    day\_of\_week(0-6) -->
|\*  |\*   |\*   |\*   |\*   |
|:--|:--|:--|:--|:--|
|min(0-59)   |hours(0-23)   |day(1-31)   |month(1-12)   |day\_of\_week(0-6)   |

