package dbconfig

import "fmt"

type Article struct {
	ID    int
	Title string
	Body  []byte
}

const PostgresDriver = "postgres"

const User = "teste"

const Host = "localhost"

const Port = "5432"

const Password = "teste"

const DbName = "teste"

const TableName = "article"

var DataSourceName = fmt.Sprintf("host=%s port=%s user=%s password=%s dbname=%s sslmode=disable", Host, Port, User, Password, DbName)