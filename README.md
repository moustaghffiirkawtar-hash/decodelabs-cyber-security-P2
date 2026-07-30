# Caesar Cipher

A simple desktop GUI for encrypting and decrypting text using a Caesar cipher with a fixed shift of 4 and case reversal.

Built with Python and `tkinter`.

---

## How it works

Each alphabetic character is shifted by 4 positions in the alphabet. On top of the shift, the case of every letter is flipped — uppercase becomes lowercase and vice versa. Non-alphabetic characters (spaces, punctuation, digits) are passed through unchanged.

**Example:**

```
Input:   Hello, World!
Encrypted: lipps, Asvph!
```

Decryption reverses the process: shift back by 4 and flip case again.

---

## Requirements

- Python 3.x
- `tkinter` (included in most standard Python installations)

---

## Usage

```bash
python caesar_cipher.py
```

1. Type your text into the input field.
2. Select **Encrypt** or **Decrypt**.
3. Click **Go**.
4. The result appears below in green (encrypt) or orange (decrypt).

---

## File structure

```
caesar_cipher.py   # Single-file application
```

---

## Functions

| Function             | Description                                           |
| -------------------- | ----------------------------------------------------- |
| `cypherchar(c)`      | Shifts a single character forward by 4                |
| `cyphertext(text)`   | Encrypts a full string with case reversal             |
| `decypherchar(c)`    | Shifts a single character back by 4                   |
| `decyphertext(text)` | Decrypts a full string with case reversal             |
| `process()`          | Reads the input field and runs the selected operation |

---

## Notes

- The shift value is hardcoded as `4`. To change it, update the `shift` variable inside `cypherchar` and `decypherchar`.
- The cipher is symmetric with case reversal: encrypting an already-encrypted string **will not** return the original — you must use Decrypt for that.
