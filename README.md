# TikTok Automation Script

A Python script to automate video checks on TikTok. This tool allows users to determine whether they are following a certain account and to unlike videos accordingly.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Language Support](#language-support)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Profile Management**: Utilizes a specific Chrome profile, defined in 'ttaut'.
- **Multilingual Support**: Recognizes the "following" status in different languages.
- **Custom Checks**: Users can specify the number of videos to check.

## Installation

Clone the repository and install the required dependencies.

**Requirements:**

- `colorama==0.4.4`
- `selenium==3.141.0`

## Usage

Simply run the script:

\`\`\`bash
python main.py
\`\`\`

1. **Set Number of Checks**: The script will prompt you to enter the number of videos you want to check.
2. **Login via Google**: A browser window will open. Navigate to TikTok via Google and log in to your account.
3. **Confirm Login**: Type 'yes' in the terminal to continue once logged in.
4. **Manual Captcha Handling**: If a captcha blocks the like button, you'll be prompted to handle it manually.

### Code References

- **Multilingual Support**: The script can detect the following status in multiple languages:

    \`\`\`python
    following_texts = ['Following', 'Volgend', 'Folge ich', 'Seguindo', 'Siguiendo', 'Abonné']
    \`\`\`

- **Unlike Videos**: If not following, the script will unlike the video:

    \`\`\`python
    if not any(follow_text in follow_button.text for follow_text in following_texts):
        like_button.click()
        print(Fore.GREEN + 'Video is unliked.')
    \`\`\`

## Language Support

The script currently supports the following languages:
- English
- Dutch
- German
- Portuguese
- Spanish
- French

To add more languages, simply extend the `following_texts` list.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to open a PR or an issue.

## License

MIT License. See `LICENSE` for more information.
