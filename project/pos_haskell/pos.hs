import Data.Time.Clock
import Data.Time.Calendar

-- Define a constant Float called taxRate as 0.065
taxRate :: Float
taxRate = 0.065

digitize :: Integer -> [Integer]
digitize 0 = []
digitize x = digitize (x `div` 10) ++ [x `mod` 10]

cardType :: Integer -> String
cardType x | (head (digitize x)) == 4 = "Visa"
           | (head (digitize x)) == 5 = "MasterCard"
           | (head (digitize x)) == 6 = "Discover"
           | otherwise = "Not Accepted"

pastDate :: Integer -> Int -> Int -> IO Bool
pastDate yr mn dy = do
  currentDay <- fmap utctDay getCurrentTime
  return((fromGregorian yr mn dy) < currentDay)

calcTax :: Float -> Float
calcTax item = item * taxRate

verifyCard :: Integer -> Integer -> Int -> Int -> IO Bool
verifyCard cardNo year month day = do
  accepted <- pastDate year month day
  return (not(accepted) && (cardType cardNo /= "Not Accepted"))

-- user input with MONADS
checkOut :: Float -> IO ()
checkOut num = do
    putStrLn "Enter cost: "
    cost <- getLine
    -- reading whatever into a float
    let amount = (read cost :: Float)
    if amount /= 0
      then do putStrLn (show amount)
              checkOut (amount + num)
    else putStrLn (show (amount + (num + (calcTax (amount + num)))))
