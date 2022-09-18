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
> ^

## Typing Comparison

<table border="0" class="grid" style="font-size: 75%;">
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

- Improved Unicode support
- Iterators everywhere
- No new features are added to Python 2

Note:

Python 3 forces the developer to explicitly make the difference between "text"
and "bytes". The developer is in full control and it reduces the risk of
byte-level bugs.

Additionally, Python 3 makes increased use of "iterators", for example in the
functions [map()][map] and [filter()][filter].

Finally, new features like [asyncio][asyncio] and “f-strings” will only be
introduced in Python 3.

[map]: https://docs.python.org/3/library/functions.html#map
[filter]: https://docs.python.org/3/library/functions.html#filter
[asyncio]: https://docs.python.org/3/library/asyncio.html#module-asyncio

Legacy platforms may only support Python 2.

<!-- .element: class="admonition note" -->

^

### Python 2 - End of Life: 2020

There is no longer an excuse to use Python 2!
^

## Strings & Bytes

<table class="grid" border="1">
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

- Always prefix text with `u` in Python 2. <p class="smallnote">Unless you know exactly that you want bytes!</p>
- Never use `encode` on bytes.
- Never use `decode` on strings.
