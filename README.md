# Mechanism to check for ESLint rules that are out of date.

**Libraries used:**
-Beautiful Soup 
-Time
-Requests

**Version Check**
-Version to check for the latest eslint version is taken from their github repo uing the github api.

https://api.github.com/repos/eslint/eslint/releases

The rules are then taken and checked by scraping the rules website of eslint and going through the rules page.

The .eslintrc.json files is checked for  deprecated or removed rules and suggestion for the neweer version of them is provided alongside the previous version, along with that every new thing is .

### Test 1:
**Input Used:**
eslint version- 4.19.1
**rules used -**
    indent
    linebreak-style
    quotes
    semi
    indent-legacy
    generator-star

**Sample Output:-**


4.19.1

You are using version 4.19.1 but latest version is 5.13.0

These rules have been deprecated and following is there newer version

indent-legacy : indent

generator-star : generator-star-spacing

Here are a list of eslint rules that you are not using yet 

['for-direction', 'getter-return', 'no-async-promise-executor', 'no-await-in-loop', 'no-compare-neg-zero', 'no-cond-assign', 'no-console', 'no-constant-condition', 'no-control-regex', 'no-debugger', 'no-dupe-args', 'no-dupe-keys', 'no-duplicate-case', 'no-empty', 'no-empty-character-class', 'no-ex-assign', 'no-extra-boolean-cast', 'no-extra-parens', 'no-extra-semi', 'no-func-assign', 'no-inner-declarations', 'no-invalid-regexp', 'no-irregular-whitespace', 'no-misleading-character-class', 'no-obj-calls', 'no-prototype-builtins', 'no-regex-spaces', 'no-sparse-arrays', 'no-template-curly-in-string', 'no-unexpected-multiline', 'no-unreachable', 'no-unsafe-finally', 'no-unsafe-negation', 'require-atomic-updates', 'use-isnan', 'valid-typeof', 'accessor-pairs', 'array-callback-return', 'block-scoped-var', 'class-methods-use-this', 'complexity', 'consistent-return', 'curly', 'default-case', 'dot-location', 'dot-notation', 'eqeqeq', 'guard-for-in', 'max-classes-per-file', 'no-alert', 'no-caller', 'no-case-declarations', 'no-div-regex', 'no-else-return', 'no-empty-function', 'no-empty-pattern', 'no-eq-null', 'no-eval', 'no-extend-native', 'no-extra-bind', 'no-extra-label', 'no-fallthrough', 'no-floating-decimal', 'no-global-assign', 'no-implicit-coercion', 'no-implicit-globals', 'no-implied-eval', 'no-invalid-this', 'no-iterator', 'no-labels', 'no-lone-blocks', 'no-loop-func', 'no-magic-numbers', 'no-multi-spaces', 'no-multi-str', 'no-new', 'no-new-func', 'no-new-wrappers', 'no-octal', 'no-octal-escape', 'no-param-reassign', 'no-proto', 'no-redeclare', 'no-restricted-properties', 'no-return-assign', 'no-return-await', 'no-script-url', 'no-self-assign', 'no-self-compare', 'no-sequences', 'no-throw-literal', 'no-unmodified-loop-condition', 'no-unused-expressions', 'no-unused-labels', 'no-useless-call', 'no-useless-catch', 'no-useless-concat', 'no-useless-escape', 'no-useless-return', 'no-void', 'no-warning-comments', 'no-with', 'prefer-promise-reject-errors', 'radix', 'require-await', 'require-unicode-regexp', 'vars-on-top', 'wrap-iife', 'yoda', 'strict', 'init-declarations', 'no-delete-var', 'no-label-var', 'no-restricted-globals', 'no-shadow', 'no-shadow-restricted-names', 'no-undef', 'no-undef-init', 'no-undefined', 'no-unused-vars', 'no-use-before-define', 'callback-return', 'global-require', 'handle-callback-err', 'no-buffer-constructor', 'no-mixed-requires', 'no-new-require', 'no-path-concat', 'no-process-env', 'no-process-exit', 'no-restricted-modules', 'no-sync', 'array-bracket-newline', 'array-bracket-spacing', 'array-element-newline', 'block-spacing', 'brace-style', 'camelcase', 'capitalized-comments', 'comma-dangle', 'comma-spacing', 'comma-style', 'computed-property-spacing', 'consistent-this', 'eol-last', 'func-call-spacing', 'func-name-matching', 'func-names', 'func-style', 'function-paren-newline', 'id-blacklist', 'id-length', 'id-match', 'implicit-arrow-linebreak', 'jsx-quotes', 'key-spacing', 'keyword-spacing', 'line-comment-position', 'lines-around-comment', 'lines-between-class-members', 'max-depth', 'max-len', 'max-lines', 'max-lines-per-function', 'max-nested-callbacks', 'max-params', 'max-statements', 'max-statements-per-line', 'multiline-comment-style', 'multiline-ternary', 'new-cap', 'new-parens', 'newline-per-chained-call', 'no-array-constructor', 'no-bitwise', 'no-continue', 'no-inline-comments', 'no-lonely-if', 'no-mixed-operators', 'no-mixed-spaces-and-tabs', 'no-multi-assign', 'no-multiple-empty-lines', 'no-negated-condition', 'no-nested-ternary', 'no-new-object', 'no-plusplus', 'no-restricted-syntax', 'no-tabs', 'no-ternary', 'no-trailing-spaces', 'no-underscore-dangle', 'no-unneeded-ternary', 'no-whitespace-before-property', 'nonblock-statement-body-position', 'object-curly-newline', 'object-curly-spacing', 'object-property-newline', 'one-var', 'one-var-declaration-per-line', 'operator-assignment', 'operator-linebreak', 'padded-blocks', 'padding-line-between-statements', 'prefer-object-spread', 'quote-props', 'semi-spacing', 'semi-style', 'sort-keys', 'sort-vars', 'space-before-blocks', 'space-before-function-paren', 'space-in-parens', 'space-infix-ops', 'space-unary-ops', 'spaced-comment', 'switch-colon-spacing', 'template-tag-spacing', 'unicode-bom', 'wrap-regex', 'arrow-body-style', 'arrow-parens', 'arrow-spacing', 'constructor-super', 'generator-star-spacing', 'no-class-assign', 'no-confusing-arrow', 'no-const-assign', 'no-dupe-class-members', 'no-duplicate-imports', 'no-new-symbol', 'no-restricted-imports', 'no-this-before-super', 'no-useless-computed-key', 'no-useless-constructor', 'no-useless-rename', 'no-var', 'object-shorthand', 'prefer-arrow-callback', 'prefer-const', 'prefer-destructuring', 'prefer-numeric-literals', 'prefer-rest-params', 'prefer-spread', 'prefer-template', 'require-yield', 'rest-spread-spacing', 'sort-imports', 'symbol-description', 'template-curly-spacing', 'yield-star-spacing']


### Test 2:
**Input Used:**
eslint version- 5.13.0
**rules used -**
    indent
    linebreak-style
    quotes
    semi
    indent-legacy
    generator-star

**Sample Output:-**

5.13.0

You are using latest version
These rules have been deprecated and following is there newer version

indent-legacy : indent

generator-star : generator-star-spacing


You can still use these rules which you havent used yet

['for-direction', 'getter-return', 'no-async-promise-executor', 'no-await-in-loop', 'no-compare-neg-zero', 'no-cond-assign', 'no-console', 'no-constant-condition', 'no-control-regex', 'no-debugger', 'no-dupe-args', 'no-dupe-keys', 'no-duplicate-case', 'no-empty', 'no-empty-character-class', 'no-ex-assign', 'no-extra-boolean-cast', 'no-extra-parens', 'no-extra-semi', 'no-func-assign', 'no-inner-declarations', 'no-invalid-regexp', 'no-irregular-whitespace', 'no-misleading-character-class', 'no-obj-calls', 'no-prototype-builtins', 'no-regex-spaces', 'no-sparse-arrays', 'no-template-curly-in-string', 'no-unexpected-multiline', 'no-unreachable', 'no-unsafe-finally', 'no-unsafe-negation', 'require-atomic-updates', 'use-isnan', 'valid-typeof', 'accessor-pairs', 'array-callback-return', 'block-scoped-var', 'class-methods-use-this', 'complexity', 'consistent-return', 'curly', 'default-case', 'dot-location', 'dot-notation', 'eqeqeq', 'guard-for-in', 'max-classes-per-file', 'no-alert', 'no-caller', 'no-case-declarations', 'no-div-regex', 'no-else-return', 'no-empty-function', 'no-empty-pattern', 'no-eq-null', 'no-eval', 'no-extend-native', 'no-extra-bind', 'no-extra-label', 'no-fallthrough', 'no-floating-decimal', 'no-global-assign', 'no-implicit-coercion', 'no-implicit-globals', 'no-implied-eval', 'no-invalid-this', 'no-iterator', 'no-labels', 'no-lone-blocks', 'no-loop-func', 'no-magic-numbers', 'no-multi-spaces', 'no-multi-str', 'no-new', 'no-new-func', 'no-new-wrappers', 'no-octal', 'no-octal-escape', 'no-param-reassign', 'no-proto', 'no-redeclare', 'no-restricted-properties', 'no-return-assign', 'no-return-await', 'no-script-url', 'no-self-assign', 'no-self-compare', 'no-sequences', 'no-throw-literal', 'no-unmodified-loop-condition', 'no-unused-expressions', 'no-unused-labels', 'no-useless-call', 'no-useless-catch', 'no-useless-concat', 'no-useless-escape', 'no-useless-return', 'no-void', 'no-warning-comments', 'no-with', 'prefer-promise-reject-errors', 'radix', 'require-await', 'require-unicode-regexp', 'vars-on-top', 'wrap-iife', 'yoda', 'strict', 'init-declarations', 'no-delete-var', 'no-label-var', 'no-restricted-globals', 'no-shadow', 'no-shadow-restricted-names', 'no-undef', 'no-undef-init', 'no-undefined', 'no-unused-vars', 'no-use-before-define', 'callback-return', 'global-require', 'handle-callback-err', 'no-buffer-constructor', 'no-mixed-requires', 'no-new-require', 'no-path-concat', 'no-process-env', 'no-process-exit', 'no-restricted-modules', 'no-sync', 'array-bracket-newline', 'array-bracket-spacing', 'array-element-newline', 'block-spacing', 'brace-style', 'camelcase', 'capitalized-comments', 'comma-dangle', 'comma-spacing', 'comma-style', 'computed-property-spacing', 'consistent-this', 'eol-last', 'func-call-spacing', 'func-name-matching', 'func-names', 'func-style', 'function-paren-newline', 'id-blacklist', 'id-length', 'id-match', 'implicit-arrow-linebreak', 'jsx-quotes', 'key-spacing', 'keyword-spacing', 'line-comment-position', 'lines-around-comment', 'lines-between-class-members', 'max-depth', 'max-len', 'max-lines', 'max-lines-per-function', 'max-nested-callbacks', 'max-params', 'max-statements', 'max-statements-per-line', 'multiline-comment-style', 'multiline-ternary', 'new-cap', 'new-parens', 'newline-per-chained-call', 'no-array-constructor', 'no-bitwise', 'no-continue', 'no-inline-comments', 'no-lonely-if', 'no-mixed-operators', 'no-mixed-spaces-and-tabs', 'no-multi-assign', 'no-multiple-empty-lines', 'no-negated-condition', 'no-nested-ternary', 'no-new-object', 'no-plusplus', 'no-restricted-syntax', 'no-tabs', 'no-ternary', 'no-trailing-spaces', 'no-underscore-dangle', 'no-unneeded-ternary', 'no-whitespace-before-property', 'nonblock-statement-body-position', 'object-curly-newline', 'object-curly-spacing', 'object-property-newline', 'one-var', 'one-var-declaration-per-line', 'operator-assignment', 'operator-linebreak', 'padded-blocks', 'padding-line-between-statements', 'prefer-object-spread', 'quote-props', 'semi-spacing', 'semi-style', 'sort-keys', 'sort-vars', 'space-before-blocks', 'space-before-function-paren', 'space-in-parens', 'space-infix-ops', 'space-unary-ops', 'spaced-comment', 'switch-colon-spacing', 'template-tag-spacing', 'unicode-bom', 'wrap-regex', 'arrow-body-style', 'arrow-parens', 'arrow-spacing', 'constructor-super', 'generator-star-spacing', 'no-class-assign', 'no-confusing-arrow', 'no-const-assign', 'no-dupe-class-members', 'no-duplicate-imports', 'no-new-symbol', 'no-restricted-imports', 'no-this-before-super', 'no-useless-computed-key', 'no-useless-constructor', 'no-useless-rename', 'no-var', 'object-shorthand', 'prefer-arrow-callback', 'prefer-const', 'prefer-destructuring', 'prefer-numeric-literals', 'prefer-rest-params', 'prefer-spread', 'prefer-template', 'require-yield', 'rest-spread-spacing', 'sort-imports', 'symbol-description', 'template-curly-spacing', 'yield-star-spacing']
