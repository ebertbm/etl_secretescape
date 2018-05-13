#!/usr/bin/env bash
psql postgres <<<"CREATE USER eberto WITH PASSWORD 'qwerty'; CREATE DATABASE secretescapes OWNER eberto; GRANT ALL PRIVILEGES ON DATABASE secretescapes to eberto";

psql postgres <<<"
        \connect secretescapes;
        DROP TABLE bookings;
        CREATE TABLE bookings (
            id                              varchar(16),
            saleName                        varchar(256),
            offerName                       varchar(600),
            departureAirportCode            varchar(80),
            departureAirportName            varchar(256),
            adults                          int,
            children                        int,
            infants                         int,
            county                          varchar(80),
            checkIn                         date,
            checkOut                        date,
            rooms                           int,
            currency                        varchar(3),
            type                            varchar(80),
            transactionId                   varchar(80),
            destinationName                 varchar(256),
            destinationType                 varchar(80),
            country                         varchar(256),
            division                        varchar(256),
            city                            varchar(256),
            providerName                    varchar(256),
            platformName                    varchar(256)
        );

        DROP TABLE sales;
        CREATE TABLE sales (
            id                             varchar(16),
            title                          varchar(256),
            sale_title                     varchar(600),
            start_date                     timestamp,
            end_date                       timestamp,
            url                            text,
            destination_type               varchar(80),
            destination_name               varchar(256),
            rate                           numeric,
            defaultCurrencyRate            numeric,
            discount                       numeric,
            discount_value                 numeric,
            description                    text,
            image                          text,
            image_thumb                    text,
            image_medium                   text,
            county                         varchar(80),
            country                        varchar(256),
            division                       varchar(256),
            city                           varchar(256),
            city_district                  varchar(256),
            product_type                   varchar(256),
            travel                         varchar(256),
            highlights                     text

        );
"
#category                       text[][],
#images                         text[][],
#price_from                     numeric