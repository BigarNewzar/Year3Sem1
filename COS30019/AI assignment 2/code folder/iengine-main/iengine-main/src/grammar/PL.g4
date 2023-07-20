grammar PL;

options
{
    language = Python3;
}

program: ( ( hornStatement | NEWLINE )* | ( statement | NEWLINE )* ) EOF;

statement: 'TELL' NEWLINE ( sentence ';' )* NEWLINE # Tell
           | 'ASK' NEWLINE sentence NEWLINE # Ask
           | 'REMOVE' NEWLINE sentence NEWLINE # Remove
           ;

hornStatement: 'TELL' NEWLINE ( hornClause ';' )* NEWLINE # HornTell
                | 'ASK' NEWLINE query=(VALUE | SYMBOL)? NEWLINE # HornAsk
                ;

hornClause: hornClauseHead IMPLICATION hornClauseTail # HornProper
            | atom=SYMBOL # HornSingle
            ;

hornClauseHead: SYMBOL ( CONJUNCTION SYMBOL )*;
hornClauseTail: VALUE | SYMBOL;

sentence: '(' sentence ')' # Nested
        | NEGATION sentence # Negation
        | lhs=sentence CONJUNCTION rhs=sentence # Conjunction
        | lhs=sentence DISJUNCTION rhs=sentence # Disjunction
        | lhs=sentence IMPLICATION rhs=sentence # Implication
        | lhs=sentence BICONDITIONAL rhs=sentence # Biconditional
        | val=VALUE # TruthLiteral
        | atom=SYMBOL # Atom
        ;

VALUE: 'True' | 'False';
SYMBOL: [A-Za-z]+[0-9]*;
CONJUNCTION: '&';
DISJUNCTION: '||';
NEGATION: '~';
IMPLICATION: '=>';
BICONDITIONAL: '<=>';
NEWLINE: [\n];
WHITESPACE: [ \t\r]+ -> skip;
