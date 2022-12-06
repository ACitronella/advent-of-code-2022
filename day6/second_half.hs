import System.IO

multihead:: [a] -> Integer -> [a]
multihead [] _ = []
multihead _ 0 = []
multihead (x:xs) n = x : (multihead xs (n-1)) 

convn:: [a] -> Integer -> [[a]]

convn all@(s:st) n | (length all) < (fromIntegral n) = []
                   | otherwise        = (multihead all n) : (convn st n)

f:: [char] ->[[char]]
f (x : y : z : []) = []
f all@(x : y : z : w : xs) = [x, y, z, w]:(f $ tail all)

__find_duplicate__:: Eq a => a -> [a] -> Bool
__find_duplicate__ _ [] = False
__find_duplicate__ c (x:xs) = (x == c) || (__find_duplicate__ c xs)

find_duplicate:: Eq a => [a] -> Bool
find_duplicate []  = False
find_duplicate (x:xs) = (__find_duplicate__ x xs) || (find_duplicate xs)

find_duplicate_with_num:: Eq a => ([a], Integer) -> Integer
find_duplicate_with_num (str, idx) | find_duplicate str = -1
                                   | otherwise = idx


main::IO()
main = do
    file <- openFile "input.txt" ReadMode
    contents <- hGetContents file
    
    let n = 14
    let s = convn contents n
    print $ head $ filter (/= -1) $ map find_duplicate_with_num (zip s [n..]) 

    hClose file