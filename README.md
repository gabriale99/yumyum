# yumyum

Currently hosting on https://d2pazxb1f1wusv.cloudfront.net/

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

### Run Unit Tests with [Vitest](https://vitest.dev/)

```sh
npm run test:unit
```

### Run End-to-End Tests with [Cypress](https://www.cypress.io/)

```sh
npm run test:e2e:dev
```

This runs the end-to-end tests against the Vite development server.
It is much faster than the production build.

But it's still recommended to test the production build with `test:e2e` before deploying (e.g. in CI environments):

```sh
npm run build
npm run test:e2e
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```
### Run Unit Tests for Serveless functions in the root directory

Make sure to install the right packages first

Window 
```sh
pip3 install -r .\requirements.txt
```

Linux 
```sh
pip3 install -r requirements.txt
```

Also ask for access key and secret access key from admin and add
it through aws configure

```sh
aws configure
```

After all the setup, run the following command

```sh
bash run_test.sh
```

For more detail on the test result, go to API/unit_tests/htmlcov
open the index.html and see the report