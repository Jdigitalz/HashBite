#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import hashlib
from rich.console import Console
from rich.spinner import Spinner
from prompt_toolkit import prompt

console = Console()

def banner(): 
    with open("assets/banner.txt", "r") as f: 
        artwork = f.read().strip()
        console.print(f"[red]{artwork}[/red]")
        
def hash_options(): 
    print("[1] sha1     [5] sha512   [9] sha3_512  [13] shake_256")
    print("[2] sha224   [6] sha3_224 [10] blake2b  [14] md5")
    print("[3] sha256   [7] sha3_256 [11] blake2s")
    print("[4] sha384   [8] sha3_384 [12] shake_128")

def generate_hash(number_or_name, input_string):
    hash_dict = {1: "sha1", 2: "sha224", 3: "sha256", 4: "sha384", 5: "sha512", 6: "sha3_224", 7: "sha3_256", 8: "sha3_384", 9: "sha3_512", 10: "blake2b", 11: "blake2s", 12: "shake_128", 13: "shake_256", 14: "md5"}
    reversed_dict = {v: k for k, v in hash_dict.items()}
    if isinstance(number_or_name, int):
        hash_algo = hash_dict.get(number_or_name)
    elif isinstance(number_or_name, str):
        hash_algo = hash_dict.get(reversed_dict.get(number_or_name, None))
    if hash_algo is None:
        raise ValueError("Invalid hash algorithm input")
    hash_object = hashlib.new(hash_algo)
    hash_object.update(input_string.encode())
    return hash_object.hexdigest()

def crack_hash(hash_alg, wordlist, hash_key): 
    banner()
    print("")
    console.print("[green]Ctrl + c to stop and go back to main menu[/green]")
    print("-" * 100)
    try: 
        console.print(f"hash type[red]: {hash_dict[hash_alg]}[/red]     |     wordlist[red]: {wordlist}[/red]     |     hash key: [red]{hash_key}[/red]")
    except KeyError:
        console.print(f"hash type[red]: {hash_alg}[/red]     |     [red]wordlist: {wordlist}[/red]     |     [red]hash key: {hash_key}[/red]")
    print("-" * 100) 
    print("Cracking hash...")
    #wlen = len(open(wordlist, "r", errors='replace').readlines())
    spinner = Spinner("line", "Cracking Hash...")  
    with console.status(spinner, spinner_style="red"):  
        with open(wordlist, "r", errors="replace") as wlist:
            for line_num, line in enumerate(wlist, 1): 
                line = line.strip()
                hashed_data = generate_hash(hash_alg, line)
                if hashed_data == hash_key:
                    console.print(f"HASH WAS FOUND: [bright_red]{line}[/bright_red]")
                    sys.exit()
            else:
                print("No matching hash found in the wordlist.")
                sys.exit()

def valid_hash(): 
    global hash_key
    banner()
    print("")
    console.print("[green]Ctrl + c to go back to main menu[/green]")
    print("-"*100)
    try:
        console.print(f"hash type[red]:{hash_dict[hash_alg]}[/red]     |     wordlist[red]:{pre_wordlists[opt_wordlist]}[/red]     |     hash key[red]:[/red]")
    except KeyError: 
        console.print(f"hash type[red]:{hash_dict[hash_alg]}[/red]     |     wordlist[red]:{os.path.basename(opt_wordlist)}[/red]     |     hash key[red]:[/red]") 
    print("-"*100)
    console.print("input hash value to start cracking")
    hash_type = hash_dict[hash_alg]
    try: 
        wordlist_dir = pre_wordlists[opt_wordlist]
    except Exception:
        wordlist_dir = opt_wordlist
    while True: 
        hash_key = prompt(">>> ").strip().lower()
        print("\033c")
        crack_hash(hash_type, wordlist_dir, hash_key)

def wordlist_options(): 
    global opt_wordlist, pre_wordlists
    pre_wordlists = {
    '1': "wordlists/rockyou.txt", 
    '2': "wordlists/cain-and-abel.txt", 
    '3': "wordlists/darkweb2017.txt"
    }
    banner()
    print("")
    console.print("[green]Ctrl + c to go back to main menu[/green]")
    print("-"*100)
    console.print(f"hash type[red]:{hash_dict[hash_alg]}[/red]     |     wordlist[red]:[/red]     |     hash key[red]:[/red]")
    print("-"*100)
    console.print("[cyan]what wordlists would you like to use?(paste path to wordlist for custom one)[/cyan]")
    print("[1]rockyou.txt")
    print("[2]cain&abel.txt")
    print("[3]darkweb2017.txt")
    while True: 
        opt_wordlist = prompt(">>> ").strip()
        if opt_wordlist in pre_wordlists: 
            print("\033c")
            valid_hash()
        elif opt_wordlist.startswith("/"):
            if os.path.isfile(opt_wordlist): 
                print("\033c")
                valid_hash()
            else: 
                console.print(f"[yellow]file path '{opt_wordlist}' cannot be found[/yellow]")
        else: 
            console.print(f"[yellow]invalid option {opt_wordlist}[/yellow]")

def main(): 
    global hash_dict, hash_alg, full_hash
    hash_dict = {
            1: "sha1",
            2: "sha224",
            3: "sha256",
            4: "sha384",
            5: "sha512",
            6: "sha3_224",
            7: "sha3_256",
            8: "sha3_384",
            9: "sha3_512",
            10: "blake2b",
            11: "blake2s",
            12: "shake_128",
            13: "shake_256",
            14: "md5"
        }
    try: 
        banner()
        print("")
        console.print("[green]type 'exit' to leave[/green]")
        print("-"*100)
        console.print("hash type[red]:[/red]     |     wordlist[red]:[/red]     |     hash key[red]:[/red]  ")
        print("-"*100)
        hash_options()
        while True: 
            hash_alg = prompt(">>> ").strip()
            if hash_alg.isdigit(): 
                hash_alg = int(hash_alg)
                if int(hash_alg) in hash_dict: 
                    print("\033c")
                    wordlist_options()
            elif hash_alg == "clear": 
                print("\033c")
                main()
            elif hash_alg == "exit": 
                sys.exit()
            else: 
                console.print(f"[yellow]{hash_alg} is not a option[/yellow]")
    except KeyboardInterrupt: 
        print("\033c")
        main()
if __name__ == "__main__": 
    main()

