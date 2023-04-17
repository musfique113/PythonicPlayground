{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "40032d14-98a6-4578-8b07-cb2e61ef0ee2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "4397ad06-5916-4b29-aefe-b8ed7f3559fa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Marks</th>\n",
       "      <th>Age</th>\n",
       "      <th>Gender</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Pikacu</td>\n",
       "      <td>15</td>\n",
       "      <td>15</td>\n",
       "      <td>Male</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Arikl</td>\n",
       "      <td>58</td>\n",
       "      <td>44</td>\n",
       "      <td>Female</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Dupta</td>\n",
       "      <td>77</td>\n",
       "      <td>13</td>\n",
       "      <td>Male</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Rasty</td>\n",
       "      <td>92</td>\n",
       "      <td>15</td>\n",
       "      <td>Male</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Dhrupb</td>\n",
       "      <td>33</td>\n",
       "      <td>14</td>\n",
       "      <td>Female</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Sikll</td>\n",
       "      <td>55</td>\n",
       "      <td>15</td>\n",
       "      <td>Male</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Tifu</td>\n",
       "      <td>87</td>\n",
       "      <td>14</td>\n",
       "      <td>Female</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Name  Marks  Age  Gender\n",
       "0  Pikacu     15   15    Male\n",
       "1   Arikl     58   44  Female\n",
       "2   Dupta     77   13    Male\n",
       "3   Rasty     92   15    Male\n",
       "4  Dhrupb     33   14  Female\n",
       "5   Sikll     55   15    Male\n",
       "6    Tifu     87   14  Female"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "table1 ={'Name':['Pikacu','Arikl','Dupta','Rasty','Dhrupb','Sikll','Tifu'], 'Marks':[15,58,77,92,33,55,87],'Age':[15,44,13,15,14,15,14],'Gender':['Male','Female','Male','Male','Female','Male','Female']\n",
    "        }\n",
    "tab1=pd.DataFrame(table1)\n",
    "tab1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "63d79699-477c-43cc-8b20-a4df9404cf6f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Marks</th>\n",
       "      <th>Age</th>\n",
       "      <th>Gender</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Pikacu</td>\n",
       "      <td>15</td>\n",
       "      <td>15</td>\n",
       "      <td>Male</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Arikl</td>\n",
       "      <td>58</td>\n",
       "      <td>44</td>\n",
       "      <td>Female</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Name  Marks  Age  Gender\n",
       "0  Pikacu     15   15    Male\n",
       "1   Arikl     58   44  Female"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Display Top 3 rows of the dataset\n",
    "tab1.head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "cf407cd2-7e7d-48dc-9309-8bfc22825a31",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Marks</th>\n",
       "      <th>Age</th>\n",
       "      <th>Gender</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Dhrupb</td>\n",
       "      <td>33</td>\n",
       "      <td>14</td>\n",
       "      <td>Female</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Sikll</td>\n",
       "      <td>55</td>\n",
       "      <td>15</td>\n",
       "      <td>Male</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Tifu</td>\n",
       "      <td>87</td>\n",
       "      <td>14</td>\n",
       "      <td>Female</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Name  Marks  Age  Gender\n",
       "4  Dhrupb     33   14  Female\n",
       "5   Sikll     55   15    Male\n",
       "6    Tifu     87   14  Female"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Display least 3 rows form dataset\n",
    "tab1.tail(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "48edfe97-23ed-4e10-abfe-f7b91f509d9c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7 Rows\n",
      "4 Colum\n"
     ]
    }
   ],
   "source": [
    "#find number of Rows and colum\n",
    "tab1.shape\n",
    "\n",
    "print(tab1.shape[0],'Rows')\n",
    "print(tab1.shape[1],'Colum')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "79d34eb9-18f9-43c5-9758-ccd0cf27da2d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
