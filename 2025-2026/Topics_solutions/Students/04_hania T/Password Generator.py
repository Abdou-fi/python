from __future__ import annotations

import secrets
import string
import tkinter as tk
from dataclasses import dataclass
from tkinter import messagebox


AMBIGUOUS_CHARS = set("O0oIl1|`'\"")


class CriteriaError(ValueError):
    """Raised when password criteria are invalid."""


@dataclass(frozen=True)
class PasswordCriteria:
    length: int
    use_lowercase: bool = True
    use_uppercase: bool = True
    use_digits: bool = True
    use_symbols: bool = True
    avoid_ambiguous: bool = False


def _filter_ambiguous(chars: str) -> str:
    return "".join(ch for ch in chars if ch not in AMBIGUOUS_CHARS)


def _build_pools(criteria: PasswordCriteria) -> tuple[str, list[str]]:
    pools: list[str] = []

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.?/"

    if criteria.avoid_ambiguous:
        lowercase = _filter_ambiguous(lowercase)
        uppercase = _filter_ambiguous(uppercase)
        digits = _filter_ambiguous(digits)
        symbols = _filter_ambiguous(symbols)

    if criteria.use_lowercase:
        pools.append(lowercase)
    if criteria.use_uppercase:
        pools.append(uppercase)
    if criteria.use_digits:
        pools.append(digits)
    if criteria.use_symbols:
        pools.append(symbols)

    all_chars = "".join(pools)
    return all_chars, pools


def validate_criteria(criteria: PasswordCriteria) -> None:
    if criteria.length < 4:
        raise CriteriaError("Password length must be at least 4.")

    all_chars, pools = _build_pools(criteria)

    if not pools or not all_chars:
        raise CriteriaError("Enable at least one character type (letters/digits/symbols).")

    if criteria.length < len(pools):
        raise CriteriaError(
            f"Length ({criteria.length}) is smaller than the number of selected types ({len(pools)}). "
            "Increase length or disable some types."
        )


def generate_password(criteria: PasswordCriteria) -> str:
    validate_criteria(criteria)

    all_chars, pools = _build_pools(criteria)

    # Guarantee at least one from each selected pool
    password_chars = [secrets.choice(pool) for pool in pools]

    # Fill remaining characters from the combined pool
    remaining = criteria.length - len(password_chars)
    password_chars.extend(secrets.choice(all_chars) for _ in range(remaining))

    # Secure shuffle
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


class PasswordGeneratorApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Password Generator")
        self.root.resizable(False, False)

        # --- Variables ---
        self.length_var = tk.StringVar(value="16")
        self.lower_var = tk.BooleanVar(value=True)
        self.upper_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        self.avoid_ambiguous_var = tk.BooleanVar(value=False)

        self.output_var = tk.StringVar(value="")

        # --- Layout ---
        container = tk.Frame(root, padx=14, pady=14)
        container.grid(row=0, column=0)

        title = tk.Label(container, text="Password Generator", font=("Arial", 14, "bold"))
        title.grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 10))

        # Length
        tk.Label(container, text="Password Length:").grid(row=1, column=0, sticky="w")
        self.length_entry = tk.Entry(container, textvariable=self.length_var, width=10)
        self.length_entry.grid(row=1, column=1, sticky="w", padx=(8, 0))
        tk.Label(container, text="(4 - 128)").grid(row=1, column=2, sticky="w", padx=(8, 0))

        # Options
        options_frame = tk.LabelFrame(container, text="Options", padx=10, pady=8)
        options_frame.grid(row=2, column=0, columnspan=3, sticky="we", pady=(10, 10))

        tk.Checkbutton(options_frame, text="Include lowercase (a-z)", variable=self.lower_var).grid(
            row=0, column=0, sticky="w"
        )
        tk.Checkbutton(options_frame, text="Include uppercase (A-Z)", variable=self.upper_var).grid(
            row=1, column=0, sticky="w"
        )
        tk.Checkbutton(options_frame, text="Include digits (0-9)", variable=self.digits_var).grid(
            row=2, column=0, sticky="w"
        )
        tk.Checkbutton(options_frame, text="Include symbols (!@#$...)", variable=self.symbols_var).grid(
            row=3, column=0, sticky="w"
        )
        tk.Checkbutton(options_frame, text="Avoid ambiguous characters (O/0, l/1...)", variable=self.avoid_ambiguous_var).grid(
            row=4, column=0, sticky="w", pady=(6, 0)
        )

        # Output
        output_frame = tk.LabelFrame(container, text="Generated Password", padx=10, pady=10)
        output_frame.grid(row=3, column=0, columnspan=3, sticky="we", pady=(0, 10))

        self.output_entry = tk.Entry(output_frame, textvariable=self.output_var, width=44, font=("Consolas", 11))
        self.output_entry.grid(row=0, column=0, columnspan=3, sticky="we")
        self.output_entry.configure(state="readonly")

        # Buttons
        btn_frame = tk.Frame(container)
        btn_frame.grid(row=4, column=0, columnspan=3, sticky="we")

        self.generate_btn = tk.Button(btn_frame, text="Generate", width=12, command=self.on_generate)
        self.generate_btn.grid(row=0, column=0, padx=(0, 8))

        self.copy_btn = tk.Button(btn_frame, text="Copy", width=12, command=self.on_copy)
        self.copy_btn.grid(row=0, column=1, padx=(0, 8))

        self.clear_btn = tk.Button(btn_frame, text="Clear", width=12, command=self.on_clear)
        self.clear_btn.grid(row=0, column=2)

        tip = tk.Label(container, text="Tip: Use a password manager and never share your passwords.", fg="gray")
        tip.grid(row=5, column=0, columnspan=3, sticky="w", pady=(10, 0))

    def _set_output(self, value: str) -> None:
        self.output_entry.configure(state="normal")
        self.output_var.set(value)
        self.output_entry.configure(state="readonly")

    def on_generate(self) -> None:
        try:
            length_text = self.length_var.get().strip()
            if not length_text:
                raise CriteriaError("Please enter a password length.")

            try:
                length = int(length_text)
            except ValueError:
                raise CriteriaError("Length must be a valid integer.")

            if not (4 <= length <= 128):
                raise CriteriaError("Length must be between 4 and 128.")

            criteria = PasswordCriteria(
                length=length,
                use_lowercase=self.lower_var.get(),
                use_uppercase=self.upper_var.get(),
                use_digits=self.digits_var.get(),
                use_symbols=self.symbols_var.get(),
                avoid_ambiguous=self.avoid_ambiguous_var.get(),
            )

            password = generate_password(criteria)
            self._set_output(password)

        except CriteriaError as exc:
            messagebox.showerror("Invalid Criteria", str(exc))
        except Exception as exc:
            messagebox.showerror("Error", f"Something went wrong:\n{exc}")

    def on_copy(self) -> None:
        pwd = self.output_var.get()
        if not pwd:
            messagebox.showinfo("Copy", "Nothing to copy. Generate a password first.")
            return

        self.root.clipboard_clear()
        self.root.clipboard_append(pwd)
        self.root.update()  # Keeps clipboard after app closes
        messagebox.showinfo("Copy", "Password copied to clipboard.")

    def on_clear(self) -> None:
        self.length_var.set("16")
        self.lower_var.set(True)
        self.upper_var.set(True)
        self.digits_var.set(True)
        self.symbols_var.set(True)
        self.avoid_ambiguous_var.set(False)
        self._set_output("")
        self.length_entry.focus_set()


def main() -> None:
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
