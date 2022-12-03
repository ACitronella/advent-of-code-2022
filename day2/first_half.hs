import System.IO

split :: Eq a => a -> [a] -> [[a]]
split d [] = []
split d s = x : split d (drop 1 y) where (x,y) = span (/= d) s

-- since exhaust all possibility is easier
jajangken:: [Char] -> Int
jajangken "A X" = 4
jajangken "A Y" = 8
jajangken "A Z" = 3
jajangken "B X" = 1
jajangken "B Y" = 5
jajangken "B Z" = 9
jajangken "C X" = 7
jajangken "C Y" = 2
jajangken "C Z" = 6
jajangken _ = 0

main::IO()
main = do
    file <- openFile "input.txt" ReadMode
    -- since haskell is lazy evaluation, make sure you complete reading the file before closing it

    contents <- hGetContents file
    let s = split '\n' contents
    print $ sum $ map jajangken s

    hClose file