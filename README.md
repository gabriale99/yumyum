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
aws cloudformation deploy \
--region us-east-1 \
--template-file web-ui-stack.yaml \
--stack-name yumyum-ui \
--capabilities CAPABILITY_IAM


aws cloudformation deploy \
--region us-east-1 \
--template-file webs3bucket_with_cloudfront.yaml \
--stack-name yumyum-ui-cloudfront \
--parameter-overrides S3BucketName=yumyum-ui-websitebucket-wk7m12rje6di

Identity pool ID 
us-east-1:dc7e6ff8-3555-4f6f-ba1b-a30c5510fe13
APP Id : 2550952455058803