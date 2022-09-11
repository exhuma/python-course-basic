# Python Basics

This chapter covers the minimum you need to know to write simple Python scripts.

^

## Hello, World!

```py
print("Hello, World!")
```
^

## Variable Types

Python is “dynamically typed”. It is often quoted as “duck typing”.

  > When I see a bird that walks like a duck and swims like a duck and quacks
  > like a duck, I call that bird a duck.
  >
  > -- James Whitcomb Riley
^

## Typing Comparison

<table border="0" id="TypingTable">
  <colgroup>
    <col width="25%">
    <col width="20%">
    <col width="55%">
  </colgroup>
  <thead valign="bottom">
    <tr>
      <th>Language</th>
      <th>Typing</th>
      <th>Coercion</th>
    </tr>
  </thead>
  <tbody valign="top">
    <tr><td>Java</td>
      <td rowspan="3">Static</td>
      <td rowspan="2">Defensive 🛡️ 🛡️</td>
    </tr>
    <tr><td>C#</td>
    </tr>
    <tr><td>C++</td>
      <td rowspan="3">Defensive 🛡️</td>
    </tr>
    <tr><td>Python</td>
      <td rowspan="5">Dynamic</td>
    </tr>
    <tr><td>Ruby</td>
    </tr>
    <tr><td>C</td>
      <td>Aggressive 💣</td>
    </tr>
    <tr><td>PHP</td>
      <td rowspan="2">Aggressive 💣 💣</td>
    </tr>
    <tr><td>JavaScript</td>
    </tr>
  </tbody>
</table>
^

## Python 2 vs Python 3

* Improved Unicode support. (bytes ≠ text, developer in full control).
* Iterators everywhere ([map()][map], [filter()][filter], …).
* No new features are added to Python 2 (f.ex.: [asyncio][asyncio], “f-strings”).
* *BUT:* Legacy platforms may only support Python 2.

[map]: https://docs.python.org/3/library/functions.html#map
[filter]: https://docs.python.org/3/library/functions.html#filter
[asyncio]: https://docs.python.org/3/library/asyncio.html#module-asyncio
^

### Python 2 - End of Life: 2020

There is no longer an excuse to use Python 2!
^


## Strings & Bytes in Python 2 & 3

<table class="docutils" border="1">
  <colgroup>
    <col width="50%">
    <col width="25%">
    <col width="25%">
  </colgroup>
  <thead valign="bottom">
    <tr class="row-odd">
      <th class="head">Literal</th>
    <th class="head">Py2 Type</th>
    <th class="head">Py3 Type</th>
    </tr>
  </thead>
  <tbody valign="top">
    <tr>
      <td><code>'Hello World'</code></td>
      <td>bytes</td>
      <td>unicode</td>
    </tr>
    <tr>
      <td><code>u'Hello World'</code></td>
      <td>unicode</td>
      <td>unicode</td>
    </tr>
    <tr>
      <td><code>b'Hello World'</code></td>
      <td>bytes</td>
      <td>bytes</td>
    </tr>
  </tbody>
</table>
^

### Warning for Python 2

* Always prefix text with u in Python 2. Unless you know exactly that you
* want bytes!
* Never use encode on bytes.
* Never use decode on strings.
