# linky
Minimal webapp for storing own link list

# prerequisities
 - `tmux` (for multiplexer functionality, can be anything)
 - `python3`

## get them on OS X:

    brew install tmux python3

## get them on Ubuntu/Debian Linux:

    sudo apt-get install tmux python3
    
## get them on Fedora Linux:

    sudo dnf install tmux python3

# installation

    tmux new -s linky
    git clone https://github.com/enedil/linky.git
    cd linky
    [sudo] pip3 install -r requirements.txt
    python3 linky.py
    

# user guide

To view the list, head your browser to [localhost:5000](http://127.0.0.1:5000/).
To add a link, open in browser [http://localhost:5000/http://file.domain/url](http://127.0.0.1:5000/http://file.domain/url).
