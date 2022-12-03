import System.IO

split :: Eq a => a -> [a] -> [[a]]
split d [] = []
split d s = x : split d (drop 1 y) where (x,y) = span (/= d) s

jajangken:: [Char] -> Int
jajangken "A X" = 3
jajangken "A Y" = 4
jajangken "A Z" = 8
jajangken "B X" = 1
jajangken "B Y" = 5
jajangken "B Z" = 9
jajangken "C X" = 2
jajangken "C Y" = 6
jajangken "C Z" = 7
jajangken _ = 0

main::IO()
main = do
    file <- openFile "input.txt" ReadMode
    -- since haskell is lazy evaluation, make sure you complete reading the file before closing it

    contents <- hGetContents file
    let s = split '\n' contents
    print $ sum $ map jajangken s

    hClose file