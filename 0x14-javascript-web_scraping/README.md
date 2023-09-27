 0x14. Javascript - Web-scraping

## Overview
The objective of this project was to manipulate JSON data, use the `request` module to query APIs, and using the `fs` module to read and write to files locally.

## Requirements
* All your files will be interpreted on `Ubuntu 14.04 LTS` using `node` (version 6.10.2)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/node`
* Your code should be `semistandard` compliant (version 11.0.0). Rules of Standard + semicolons on top.
* All your files must be executable
* Not allowed to use `var` to declare variables

## Tasks
### Mandatory
**[0-readme.js](0-readme.js)** - Script that reads and prints the content of a f ile where the first argument is the file path
```
$ ./0-readme.js cisfun
C is super fun!
$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
```

**[1-writeme.js](1-writeme.js)** - Script that writes a string to a file where the first argument is the file path and the second argument is the string to write
```
$ ./1-writeme.js my_file.txt "Python is cool"
$ cat my_file.txt ; echo ""
Python is cool
```

**[2-statuscode.js](2-statuscode.js)** - Script that displays the status code of a GET request where the first argument is the URL to request and the format is `code: <status code>`
```
$ ./2-statuscode.js https://intranet.hbtn.io/status
code: 200
$ ./2-statuscode.js https://intranet.hbtn.io/doesnt_exist
code: 404
```

**[3-starwars_title.js](3-starwars_title.js)** - Script that prints the title of a Star Wars movie given the episode number as an integer. The first argument is the episode number and the API link is `http://swapi.co/api/films/:id`
```
$ ./3-starwars_title.js 1
A New Hope
$ ./3-starwars_title.js 5
Attack of the Clones
```

**[4-starwars_count.js](4-starwars_count.js)** - Script that prints the number of movies that the character "Wedge Antilles" is present in. The first argument is the API URL - `http://swapi.co/api/films/` and Wedge's ID is `18`
```
$ ./4-starwars_count.js http://swapi.co/api/films
3
```

**[5-request_store.js](5-request_store.js)** - Script that gets the contents of a webpage and stores it in a file. The first argument is the URL to request and the second argument is the file path to store the body response
```
$ ./5-request_store.js http://loripsum.net/api loripsum
$ cat loripsum
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Haec quo modo conveniant, non sane intellego. Nam memini etiam quae nolo, oblivisci non possum quae volo. Te enim iudicem aequum puto, modo quae dicat ille bene noris. Terram, mihi crede, ea lanx et maria deprimet. Deinde prima illa, quae in congressu solemus: Quid tu, inquit, huc? Hoc etsi multimodis reprehendi potest, tamen accipio, quod dant. </p>

<p>Ad eos igitur converte te, quaeso. Pudebit te, inquam, illius tabulae, quam Cleanthes sane commode verbis depingere solebat. Sic enim censent, oportunitatis esse beate vivere. Quo studio Aristophanem putamus aetatem in litteris duxisse? Aeque enim contingit omnibus fidibus, ut incontentae sint. Ut aliquid scire se gaudeant? Qui enim existimabit posse se miserum esse beatus non erit. Putabam equidem satis, inquit, me dixisse. </p>

<p>Duo Reges: constructio interrete. Quid ei reliquisti, nisi te, quoquo modo loqueretur, intellegere, quid diceret? Quis animo aequo videt eum, quem inpure ac flagitiose putet vivere? Illud non continuo, ut aeque incontentae. Illa videamus, quae a te de amicitia dicta sunt. At ille pellit, qui permulcet sensum voluptate. Tamen aberramus a proposito, et, ne longius, prorsus, inquam, Piso, si ista mala sunt, placet. </p>

<p>Non enim, si omnia non sequebatur, idcirco non erat ortus illinc. Nos cum te, M. Quem si tenueris, non modo meum Ciceronem, sed etiam me ipsum abducas licebit. Apparet statim, quae sint officia, quae actiones. Ergo instituto veterum, quo etiam Stoici utuntur, hinc capiamus exordium. Eadem nunc mea adversum te oratio est. Quid, si etiam iucunda memoria est praeteritorum malorum? Hoc enim constituto in philosophia constituta sunt omnia. </p>
```

**[6-completed_tasks.js](6-completed_tasks.js)** - Script that computes the number of tasks completed by user ID. The first argument is a link to the API `https://jsonplaceholder.typicode.com/todos`
```
$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{ '1': 11,
  '2': 8,
  '3': 7,
  '4': 6,
  '5': 12,
  '6': 6,
  '7': 9,
  '8': 11,
  '9': 8,
  '10': 12 }
```

### Advanced
**[100-starwars_characters.js](100-starwars_characters.js)** - Script that prints all characters that were in a Star Wars movie. The first argument is the movie ID as an integer
```
$ ./100-starwars_characters.js 3
Darth Vader
R2-D2
Luke Skywalker
Han Solo
Leia Organa
Chewbacca
Palpatine
Obi-Wan Kenobi
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Boba Fett
Ackbar
Arvel Crynyd
Mon Mothma
Nien Nunb
Wicket Systri Warrick
Bib Fortuna
C-3PO
Lando Calrissian
```

2021- All programs written by itsmuriuki
