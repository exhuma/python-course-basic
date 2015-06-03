.. {{{  RST definitions

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

.. }}}

.. {{{ Introduction
git
===
* |home| http://michel.albert.lu/shelf/git2015
* http://git-scm.com
* Images licensed under CC BY-NC-SA 3.0 by Scott Chacon
.. }}}

.. {{{ Outline of Version Control
What is Version Control
-----------------------

* Like "track changes" in office products. But on steroids.
* Primarily for plain-text files (f.ex.: source code).
* Visualising changes in files (diffing).
* Undo those changes easily.
* Branching, branching, branching.
* Conflict handling/resolution.

Version Control Models
----------------------

================== =======================
 Name               Model
================== =======================
 CVS                Client/Server
 SVN                Client/Server
 ClearCase          Client/Server
 Perforce           Client/Server
 TFVC (TFS)         Client/Server
 Visual SourceSafe  Client/Server
 Bazaar             Distributed
 Mercurial          Distributed
 git                Distributed
================== =======================

Distributed vs. Client/Server
-----------------------------

Centralised (Client/Server)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. ifslides::

    |br| |br|

.. image:: _static/images/centralized.png
    :align: left
    :width: 380px

.. sidebar:: Summary

    * One place to apply access rights.
    * Single point of failure


Distributed
~~~~~~~~~~~

.. ifslides::

    |br| |br|

.. image:: _static/images/distributed.png
    :align: left
    :width: 380px

.. sidebar:: Summary

    * Supports larger teams (infinite scale).
    * Access control works like a "Web of Trust".
    * No connection to server required (working off-line).
    * Can support very complex workflows (f.ex.: code-review, "tenured"
    repositories, …).


Git
---

* Fully distributed
* Stream of snapshots instead of history of deltas.

  * Latest snapshot is kept in full, backwards deltas (after packing).

* Nearly all operations executed locally (no network overhead).
* Strong integrity (SHA1 hashes of snapshot content).


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
    :caption: **Filename** ~/.gitconfig

    [user]
    name = John Doe
    email = john.doe@example.com

    [core]
    editor = vim

    [alias]
    st = status -s


Help
----

.. code-block:: bash

    $ git help <verb>
    $ git <verb> --help
    $ man git-verb
.. }}}

.. {{{ Key terms
Key Terms
---------

working copy
    The files you are working with, the files you see on your disk, your copy
    of the source-code.

index
    A "staging area" to prepare the next commit. As far as I know, unique to
    git.

commit
    A snapshot of the source code. These are points in time you can come back
    to.

repository
    This is where all the history (commits) and related metadata (tags,
    branches, …) are stored.
.. }}}

.. {{{ repo setups
Repository Setups
=================

One Reference Repo
------------------

.. image:: _static/images/centralized_workflow.png
    :align: center

.. nextslide::
    :increment:

* Very similar workflow to a centralised VCS. No new tricks to learn.
* Good for small teams.
* Easy to manage.
* Developers do not need to make their repositories public.

.. admonition:: Info

    "Public" here does not necessarily mean public to the world. It only means
    that someone else than the author has access to the repo!

    Note that instead of a public repository, git also makes it easy to
    contribute changes via e-mail.


Integration Manager
-------------------

.. image:: _static/images/integration-manager.png
    :align: center

.. nextslide::
    :increment:

* Mostly distributed.
* Integration manager has control over what patches (changes) are accepted.
* Good for projects with dynamic teams.
* Developers need to provide a public repository.


Beneveloent Dictator Model
--------------------------

.. image:: _static/images/benevolent-dictator.png
    :align: center

.. nextslide::
    :increment:

* Better control over contributed code.
* Essentially a Web of Trust (WoT).
* Good for very large projects with large teams.
* Used to manage the Linux source code.
* Developers need to provide a public repository.

.. }}}

.. {{{ Workflow
Example Workflow
----------------

.. figure:: _static/images/nvie-workflow.png
    :width: 400
    :align: center

    See: http://nvie.com/posts/a-successful-git-branching-model/

Version Numbers
---------------

* Semantic versioning (http://www.semver.org)
* Very good for application interfaces.
* More difficult for user interfaces.
* major, minor, patch

  * **major** backwards *incompatible* changes.
  * **minor** backwards compatible changes.
  * **patch** bugfixes.

Workflow Branches
-----------------

master
    One commit per release.

develop
    Ongoing work

release/*
    Feature freeze for release / metadata & doc updates

hotfix/*
    Bugfixes

feature/*
    Work on one specific feature.

.. }}}

.. {{{ essential commands

Essential Commands
------------------

``git init``
    Create an empty git repository or reinitialize an existing one

``git add``
    Add file contents to the index

``git clone``
    Clone a repository into a new directory. This is *not* the same as
    ``checkout`` in SVN!

``git status``
    Show the working tree status

.. nextslide::
    :increment:

``git pull``
    Fetches changes **from** a remote repository (f.ex. the server).

``git push``
    Sends changes **to** a remote repository (f.ex. the server).

``git commit``
    Creates a new snapshot from the index.

``git checkout``
    Gets a branch or path/file into the working directory.

``git log``
    Shows the timeline of changes.

.. nextslide::
    :increment:

``git gitk``
    Launches a graphical history browser.

``git show``
    Displays the content of any git object (commit, branch, tag, tree, …)

``git reset``
    Moves the ``HEAD`` pointer. Can be used (among other things) to drop all
    pending (non-committed) changes.

git Areas
---------

.. ifslides::

    |br| |br|

.. image:: _static/images/areas.png
    :align: center

Example Remote Interaction
--------------------------

.. ifslides::

    |br|

.. image:: _static/images/small-team-flow.png
    :align: center
    :height: 500px

.. }}}

.. {{{ intermediate git commands
.. merge
.. rebase
.. bisect
.. pickaxe
.. cherry-pick
.. }}}

.. {{{ Branching
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
.. }}}

.. {{{ Configuration
.. /etc/git -> ~/.gitconfig | ~/.config/git/config -> .git/config
.. core.editor
.. commit.template
.. core.excludesfile
.. help.autocorrect
.. merge.tool
.. diff.tool
.. core.autocrlf
.. }}}

.. {{{ hooks
.. client-side hooks -- see page 402
.. [commit] -> pre-commit -> prepare-commit-msg -> [edit msg] -> commit-msg-hook -> <commit finalized> -> post-commit
.. server-side hooks
.. [push] -> <update remote refs> -> pre-receive -> update -> <finalize push> -> post-receive?
.. }}}

.. {{{ Best practices
General Best Practices
----------------------

* Avoid publishing broken commits.
* Avoid changing the published history (``git commit --amend``, ``git rebase``,
  ``git reset``, …).
* Avoid pushing too often. As long as you have not pushed, it is okay to change
  history (see the previous point).
* Use the index to prepare coherent commits (``git add -p`` is your friend).
* Commit often. Avoid working for a week and commit all that work in one go.
  This avoids hairy conflicts.
.. }}}

.. protocols http, https, git, ssh
.. (un)tracked, unmodified, modified, staged
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
.. == ADVANCED STUFF ==
..      manual merging



.. grep       Print lines matching a pattern
.. show       Show various types of objects
.. bisect     Find by binary search the change that introduced a bug


.. {{{ --- FIN ----------------------------------------------------------------
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
.. }}}

.. vim: set foldmethod=marker :
