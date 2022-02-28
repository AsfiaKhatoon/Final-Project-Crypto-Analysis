-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "btc" (
    "Date" DATE   ,
    "Open" numeric  ,
    "High" numeric  ,
    "Close" numeric  ,
     "Adj Close" numeric,
     "Volume" numeric,
     "ds" Date ,
     "y" numeric
     PRIMARY KEY (
        "Date"
     )
);




