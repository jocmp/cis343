head' :: [Float] -> Float
head' [] = error "You failed like usual :)"
head' (arr:_) = arr

get_gpa :: Float -> String
get_gpa x | x > 4.0 = "A++ :)"
          | x == 4.0 = "A"
          | x > 3.0 = "B"
          | x > 2.0 = "C"
          | x > 1.0 = "D"
          | otherwise = "Why bother."

contrived :: String -> String
contrived y | (head y) == 'a' = y
            | (head y) == 'b' = y
            | (head y) == 'c' = y
            | otherwise = error "Can't be done. :/"

-- user input with MONADS
checkOut :: Float -> IO ()
checkOut num = do
    putStrln "Enter cost: "
    cost <- getLine
    -- reading whatever into a float
    let amount = (read cost :: Float)
    if amount /= 0
      then do putStrln (show amount)
              checkOut (amount + num)
    else putStrLn (show (amount + (num + (calcTax (amount + num)))))


-- first param is function, second is Data
-- map function data
-- map (sum x y) [(1, 1), (2, 2)]
-- L sum 1, 1
-- L sum 2, 2
-- L sum 3, 3
