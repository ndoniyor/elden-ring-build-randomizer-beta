# Elden Ring Build Randomizer Web App
Dynamic web app built with Flask that generates randomized character builds for players of the game Elden Ring. Builds can be generated with pure randomness, or biased with various build flags.

# Usage
Site is currently hosted at: http://eldenrandomizer.pythonanywhere.com

## To run locally:
1. Clone the repository: 'git clone https://github.com/ndoniyor/elden-ring-build-randomizer.git && cd elden-ring-build-randomizer'
2. Install dependencies: 'conda env create -f environment.yml'
3. Run flask app: 'flask --app web --debug run'
4. Open a web browser and navigate to http://localhost:[PORT]

# Suggestions
Feel free to create a pull request or submit an issue with suggestions for the site

# To-Do
- [ ] Add column to ash of war/sorcery/incantation csv indicating type (user can specify what kind of build)
- [x] Add column to weapon csv indicating type (user can specify what kind of weapons)
- [ ] Add full randomizer (no bias) and refined randomizer
- [x] If weapon is a bow - find bow Ash of War
- [x] Create item class so link can be stored without list
- [x] Update spells player class member to be a list of type 'item'
- [x] Split up table to be more narrow and easier to read
- [x] Delete talismans and staffs, I figure people will just go with whatever suits the spells that were chosen
- [ ] Integrate JS and Jquery for more responsive webpage

# License
Copyright 2023 Doniyor Nimatullo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

