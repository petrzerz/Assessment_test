CREATE TABLE "Customer" (
  "custNum" SERIAL PRIMARY KEY,
  "custName" varchar
);

CREATE TABLE "Billing" (
  "billNum" SERIAL PRIMARY KEY,
  "custNum" int,
  "cashierID" int
);

CREATE TABLE "Place_Order" (
  "PlaceOrderID" SERIAL PRIMARY KEY,
  "custNum" int,
  "bookID" int
);

CREATE TABLE "Category" (
  "categoryID" SERIAL PRIMARY KEY,
  "categoryName" varchar
);

CREATE TABLE "Book" (
  "bookID" SERIAL PRIMARY KEY,
  "bookName" varchar,
  "categoryID" int,
  "authorID" int,
  "publisherID" int
);

CREATE TABLE "Cashier" (
  "cashierID" SERIAL PRIMARY KEY,
  "cashierName" varchar
);

CREATE TABLE "Author" (
  "authorID" SERIAL PRIMARY KEY,
  "authorName" varchar
);

CREATE TABLE "Publisher" (
  "publisherID" SERIAL PRIMARY KEY,
  "publisherName" varchar
);

ALTER TABLE "Place_Order" ADD FOREIGN KEY ("custNum") REFERENCES "Customer" ("custNum");

ALTER TABLE "Place_Order" ADD FOREIGN KEY ("bookID") REFERENCES "Book" ("bookID");

ALTER TABLE "Book" ADD FOREIGN KEY ("categoryID") REFERENCES "Category" ("categoryID");

ALTER TABLE "Book" ADD FOREIGN KEY ("authorID") REFERENCES "Author" ("authorID");

ALTER TABLE "Book" ADD FOREIGN KEY ("publisherID") REFERENCES "Publisher" ("publisherID");

ALTER TABLE "Billing" ADD FOREIGN KEY ("cashierID") REFERENCES "Cashier" ("cashierID");

ALTER TABLE "Billing" ADD FOREIGN KEY ("custNum") REFERENCES "Customer" ("custNum");
