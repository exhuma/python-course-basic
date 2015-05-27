.. |br| raw:: html

   <br />

.. |clear| raw:: html

   <br clear="both" />

.. role:: checkpoint
    :class: checkpoint

.. role:: keyterm
    :class: keyterm

.. role:: strike
    :class: strike

.. |home| image:: _static/icons/home.png
    :class: midline

.. |github| image:: _static/icons/github-circle.png
    :class: midline

.. |gplus| image:: _static/icons/google-plus.png
    :class: midline


git
===

* |home| http://michel.albert.lu/shelf/git2015
* http://git-scm.com


Version Control
---------------

================== =======================
 Name               Model
================== =======================
 CVS                Client/Server
 SVN                Client/Server
 ClearCase          Client/Server
 Perforce           Client/Server
 TFS                Client/Server
 Visual SourceSafe  Client/Server
 Bazaar             Distributed
 Mercurial          Distributed
 git                Distributed
================== =======================


Distributed vs. Client/Server
-----------------------------

Distributed
~~~~~~~~~~~

* Supports larger teams (infinite scale).
* Access control works like a "Web of Trust".
* No connection to server required (working off-line).
* Can support very complex workflows (f.ex.: code-review, "tenured"
  repositories, …).


Centralised
~~~~~~~~~~~

* One place to apply access rights.
* Single point of failure
* Strong integrity (SHA1 hashes of snapshot content).



Git
---

* Fully distributed
* Stream of snapshots instead of History of deltas.
* Nearly all operations executed locally (no network overhead).


Installing
----------

* Linux
    .. code-block:: bash

        $ sudo yum install git
        $ sudo aptitude install git
* MacOS

  * Run XCode
  * Run ``git`` in a terminal

* Windows

  * Official client: http://git-scm.com/download/win
  * Github for Windows: http://windows.github.com


Configuration
-------------

.. code-block:: ini

    [user]
    name = John Doe
    email = john.doe@example.com

    [core]
    editor = vim


.. TODO aliases


Help
----

.. code-block:: bash

    $ git help <verb>
    $ git <verb> --help
    $ man git-verb


Basics
======
.. init       Create an empty git repository or reinitialize an existing one
.. add        Add file contents to the index
.. clone      Clone a repository into a new directory
..    clone != subversion/checkout
.. protocols http, https, git, ssh
.. (un)tracked, unmodified, modified, staged
.. status     Show the working tree status
.. hands-on -> Create a new file, view status, add it to repo
..    !!! Never add derived files (binary, minified, ...)
.. hands-on -> modify exsting file, view status, add it to repo
.. hands-on -> modify the same file again, view status, add it to repo <-- listed as staged and modified
.. hands-on -> git status --short/-s
.. .gitignore
.. diff       Show changes between commits, commit and working tree, etc
..    --staged/--cached
..    --difftool
.. commit     Record changes to the repository
..    -v
..    -a
..    $EDITOR / core.editor
.. rm         Remove files from the working tree and from the index
..    --cached
.. mv         Move or rename a file, a directory, or a symlink
..    equivalend to remove -> add
.. log        Show commit logs
..    >> git clone https://github.com/schacon/simplegit-progit
..    Author vs. Committer
..    --since/--after, --until/--before
..    --author
..    --grep (--all-match)
..    -S
..    -L
..    <from>..<to>
.. == UNDOING ==
.. reset
.. commit --amend
.. checkout -- <filename>
.. == REMOTES ==
.. remote
..      -v
..      add <shortname> <url>
..      show <shortname>
.. fetch <shortname>     Download objects and refs from another repository
.. push/fetch/merge(basic)/pull
.. tag        Create, list, delete or verify a tag object signed with GPG
..      pushing tags
.. == BRANCHING/MERGING ==
.. checkout   Checkout a branch or paths to the working tree
..      -b <localname> <base> (also creates editable branches of remote branches)
..      --track <remotename>/<branchname>
.. branch     List, create, or delete branches
..      -d / -D
.. merge(2)
..      fast-forward merge
.. == CONFLICTS ==
..      Everything above "=======" is your HEAD (merge base), everything below is what your are merging.
..      -> git add -> git commit
..      git mergetool
.. == WORKING WITH REMOTES ==
..      topic/feature branches
..      Everything is local! No server communication, no sharing!
..      Remote tracking branches
..      git fetch
..      git push (no branches created by default)!
..          <localname>:<remotename> (can be used for deleting)
..      git branch -vv
..      push origin --delete <targetbranch>
.. == REWRITING HISTORY ==
..      rebase     Forward-port local commits to the updated upstream head
..          -i
.. == ON THE SERVER ==
..      bare repositories
..      protocols
..          local
..          http(s), smart (1.6.6+)/dumb
..          ssh
..          git
..      git-shell in /etc/passwd
.. == WORKFLOWS ==
..      private shared
..      private managed
..      forked
..      email-based
.. stash



.. grep       Print lines matching a pattern
.. show       Show various types of objects
.. bisect     Find by binary search the change that introduced a bug




.. --- FIN -------------------------------------------------------------------

.. slide::
    :level: 2

    .. container:: centered

        Thank You!

        .. image:: _static/avatar.jpg
            :align: center
            :class: avatar

        Questions?

    * |home| http://michel.albert.lu
    * |github| exhuma
    * |gplus| MichelAlbert
