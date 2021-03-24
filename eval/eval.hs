module Eval where
import Data.Char (isDigit)

data Exp = Number String | Operator String | Function String | Bracket String | Comma String

splitUp :: String -> [Exp]
splitUp [] = []
splitUp (c:cs)
    | isDigit c = [result] ++ splitUp remaining
    | c == '+' = [Operator "+"] ++ splitUp cs
    | otherwise = [Operator "-"] ++ splitUp cs
    where (result, remaining) = extractNumber (c:cs) ""

extractNumber :: String -> String -> (Exp, String)
extractNumber (c:cs) acc
    | isDigit c = extractNumber cs (acc ++ [c])
    | otherwise = (Number acc, cs)