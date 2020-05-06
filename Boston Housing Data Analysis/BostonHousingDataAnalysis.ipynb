{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Project - Boston Housing Data Analysis\n",
    "***"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Introduction"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this notebook I will be analysing and evaluating data on the housing values in the suburbs of Boston, US. Most notably, looking for differences or patterns within the dataset with which I can really test out my data munging and visualisation skills.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This dataframe contains the following columns \n",
    "\n",
    "- ```crim```: per capita crime rate by town\n",
    "- ```zn```: proportion of residential land zoned for lots over 25,000 sq ft\n",
    "- ```indus```: proportion of non-retail business acres per town\n",
    "- ```chas```: Charles river dummy variable (= 1 if tract bounds river; 0 otherwise)\n",
    "- ```nox```: nitrogen oxide concentration (parts per 10 million)\n",
    "- ```rm```: average number of rooms per dwelling\n",
    "- ```age```: proportion of owner-occupied units built prior to 1940\n",
    "- ```dis```: weighted mean of distances to five Boston employment centers\n",
    "- ```rad```: index of accessibility to radial highways\n",
    "- ```tax```: full-value property-tax rate per \\\\$10,000\n",
    "- ```ptratio```: pupil-teacher ratio by town\n",
    "- ```b```: 1000(Bk - 0.63)^2 where Bk is the proportion of African American individuals by town\n",
    "- ```lstat```: lower status of the population (percent)\n",
    "- ```medv```: median value of owner-occupied homes in $10000s\n",
    "\n",
    "***\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "333\n"
     ]
    },
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
       "      <th>ID</th>\n",
       "      <th>crim</th>\n",
       "      <th>zn</th>\n",
       "      <th>indus</th>\n",
       "      <th>chas</th>\n",
       "      <th>nox</th>\n",
       "      <th>rm</th>\n",
       "      <th>age</th>\n",
       "      <th>dis</th>\n",
       "      <th>rad</th>\n",
       "      <th>tax</th>\n",
       "      <th>ptratio</th>\n",
       "      <th>black</th>\n",
       "      <th>lstat</th>\n",
       "      <th>medv</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0.00632</td>\n",
       "      <td>18.0</td>\n",
       "      <td>2.31</td>\n",
       "      <td>0</td>\n",
       "      <td>0.538</td>\n",
       "      <td>6.575</td>\n",
       "      <td>65.2</td>\n",
       "      <td>4.0900</td>\n",
       "      <td>1</td>\n",
       "      <td>296</td>\n",
       "      <td>15.3</td>\n",
       "      <td>396.90</td>\n",
       "      <td>4.98</td>\n",
       "      <td>24.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>0.02731</td>\n",
       "      <td>0.0</td>\n",
       "      <td>7.07</td>\n",
       "      <td>0</td>\n",
       "      <td>0.469</td>\n",
       "      <td>6.421</td>\n",
       "      <td>78.9</td>\n",
       "      <td>4.9671</td>\n",
       "      <td>2</td>\n",
       "      <td>242</td>\n",
       "      <td>17.8</td>\n",
       "      <td>396.90</td>\n",
       "      <td>9.14</td>\n",
       "      <td>21.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4</td>\n",
       "      <td>0.03237</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2.18</td>\n",
       "      <td>0</td>\n",
       "      <td>0.458</td>\n",
       "      <td>6.998</td>\n",
       "      <td>45.8</td>\n",
       "      <td>6.0622</td>\n",
       "      <td>3</td>\n",
       "      <td>222</td>\n",
       "      <td>18.7</td>\n",
       "      <td>394.63</td>\n",
       "      <td>2.94</td>\n",
       "      <td>33.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>5</td>\n",
       "      <td>0.06905</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2.18</td>\n",
       "      <td>0</td>\n",
       "      <td>0.458</td>\n",
       "      <td>7.147</td>\n",
       "      <td>54.2</td>\n",
       "      <td>6.0622</td>\n",
       "      <td>3</td>\n",
       "      <td>222</td>\n",
       "      <td>18.7</td>\n",
       "      <td>396.90</td>\n",
       "      <td>5.33</td>\n",
       "      <td>36.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>7</td>\n",
       "      <td>0.08829</td>\n",
       "      <td>12.5</td>\n",
       "      <td>7.87</td>\n",
       "      <td>0</td>\n",
       "      <td>0.524</td>\n",
       "      <td>6.012</td>\n",
       "      <td>66.6</td>\n",
       "      <td>5.5605</td>\n",
       "      <td>5</td>\n",
       "      <td>311</td>\n",
       "      <td>15.2</td>\n",
       "      <td>395.60</td>\n",
       "      <td>12.43</td>\n",
       "      <td>22.9</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   ID     crim    zn  indus  chas    nox     rm   age     dis  rad  tax  \\\n",
       "0   1  0.00632  18.0   2.31     0  0.538  6.575  65.2  4.0900    1  296   \n",
       "1   2  0.02731   0.0   7.07     0  0.469  6.421  78.9  4.9671    2  242   \n",
       "2   4  0.03237   0.0   2.18     0  0.458  6.998  45.8  6.0622    3  222   \n",
       "3   5  0.06905   0.0   2.18     0  0.458  7.147  54.2  6.0622    3  222   \n",
       "4   7  0.08829  12.5   7.87     0  0.524  6.012  66.6  5.5605    5  311   \n",
       "\n",
       "   ptratio   black  lstat  medv  \n",
       "0     15.3  396.90   4.98  24.0  \n",
       "1     17.8  396.90   9.14  21.6  \n",
       "2     18.7  394.63   2.94  33.4  \n",
       "3     18.7  396.90   5.33  36.2  \n",
       "4     15.2  395.60  12.43  22.9  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv('train.csv')\n",
    "print(len(df))\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 333 entries, 0 to 332\n",
      "Data columns (total 15 columns):\n",
      "ID         333 non-null int64\n",
      "crim       333 non-null float64\n",
      "zn         333 non-null float64\n",
      "indus      333 non-null float64\n",
      "chas       333 non-null int64\n",
      "nox        333 non-null float64\n",
      "rm         333 non-null float64\n",
      "age        333 non-null float64\n",
      "dis        333 non-null float64\n",
      "rad        333 non-null int64\n",
      "tax        333 non-null int64\n",
      "ptratio    333 non-null float64\n",
      "black      333 non-null float64\n",
      "lstat      333 non-null float64\n",
      "medv       333 non-null float64\n",
      "dtypes: float64(11), int64(4)\n",
      "memory usage: 39.1 KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exploring the dataset"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I like to explore the dataset first and foremost with some simple visualisations. I will draw on some of the specific data columns to get a feel of the society in Boston and see if anything jumps out at me"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'Number of houses')"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAZkAAAEWCAYAAAC0Q+rDAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAIABJREFUeJzt3WmYXFW59vH/TRKmJBACGCEgAQQUiSAERPBoM4gMCqgo+CImHJTjxKBhElQQB0BF4OgRRFRGyYGIDAoCQhoUZUggEGY4gMxhkEASwBB43g9rddgpqqqrO72ruqvv33X11VV7WOtZe3r2VHsrIjAzMyvDUq0OwMzM2peTjJmZlcZJxszMSuMkY2ZmpXGSMTOz0jjJmJlZaUpPMpJOk/TtPirrHZLmSRqSv3dK+kJflJ3Lu0LSxL4qrwf1fl/Sc5KebnbdZZG0t6SrWh2HtS9J4ySFpKGtjsVqW6IkI+kRSa9ImitpjqS/S/qSpEXlRsSXIuJ7DZa1fb1hIuLRiBgREa8vSdy5vmMknVtR/k4RcdaSlt3DONYEJgMbRsTbq/TvyCvSRRXdN87dO5sUarHuMyUtyPN9rqQ7JR0nacWuYSLivIjYocGyvl9uxH1nSeMtTLt5hb8hNYadJOn1wnAPSfpy76NfVO5blv2+lJfL+RVtPKys+gaSRpYfJQfm9Wq+pMclXShpfDPq72t9cSTz8YgYCawFHA8cDvy6D8pdTBvvrawFPB8Rz9QZ5llgK0krF7pNBO4vNbL6fpTn+6rAvsCWwA2ShrcwpoHiR3lnaUQDO03/6BoO2AP4kaT3NSnOJbFxRRt/1OqABpBTgIOAA4HRwPrAxcAurQwKerkdjohe/wGPANtXdNsCeAPYKH8/E/h+/rwK8EdgDvAv4K+kRHdOHucVYB5wGDAOCGA/4FHg+kK3obm8TuA44GbgReASYHTu1wE8Xi1eYEdgAfBaru/2QnlfyJ+XAr4F/BN4BjgbWDH364pjYo7tOeCoOtNpxTz+s7m8b+Xyt89tfiPHcWaVcTuAx4HTgK/mbkNyt+8AnYVh3wVcnaftfcBnCv12AW4DXgIeA44p9OtpexbN00K3kcBTwNfy90nA3/JnASfl6fgicAewEbB/ngcLcvsvy8MfAfwfMBe4G/hEoZ5JwN+AnwAvAA8DOxX6jwZ+CzyZ+19c6PcxYCZp+fs78N5Cv8OBJ3Kd9wHbVWl3rXjfnZedOcBdwK49mXZ1hl00DQvdbgb+X+H7rrnOOTmGd9drE7WX/dWBS/Oy8yDwxUI5xwAXkJbhubm+CXXiDuCdNfodA1wInJvLmkXaiH4zLx+PATsUhu+k9jo+jsW3B1XbALwdeBlYuVDuZqT1cViezjeQltE5wEPAVrn7YzmuiYVxlyEtf48Cs0nr5nIV6+vkPN5TwL71lp+K6bMe8DqwRZ3p26f15+n2+zw9HgYOrJhfU/P8egn4AmkbPz1/nw38tO5y3MjCXqexj1CRZHL3R4EvV65UeWE5Lc/YYcB/AKpWVmEBOhsYDixXZaHqJK1EG+Vhfg+cW5zYteLNE+/civ6dvJlk/pO0oK4DjAAuAs6piO1XOa6NgX9TWMEryj2btHKMzOPeD+xXK86KcbsWmq2Am3K3nYEr8wzvzN2Gk1aIfYGhwKakZPGeQjnjScntvXnh2L2X7Vk0T6u0838rN5DAR4EZwChSwnk3sFqtsoBPkxb8pYA9gfmF4SeRVpQvkpLtl0kJpWs5+hPwv8BKpGXsw7n7pqSV7v15vIl5eVgG2CBPu9UL02PdRtqe63gQOBJYGtiWtPHcoM74/8p/M4BP1Zn3i6Zh/r45aSO4fv6+fp42H8lxHJZjWbpem6i+7F8H/AJYFtiEtMHZrjD8q6TlbghpPb6xTtzdJZlX8zIxNC8zDwNH5TZ8EXi4Yp2stY6PY/HtQb02XE7eJuXvJwE/K0znhaR1ZwjwfdI27H/y8rFDnqcj8vAnk5LZaNI6fRlwXGE9Wwgcm9uzMynBrVRv3SnE9SXgn91sd/usftI6NoO0w7o0aXv3EPDRwvx6Ddg9D7sc8A9gn9x/BLBl3Xjr9ezuj9pJ5kbynjCLJ5ljSRvbtyyAlWUVFqB1qnQrJpnjC/03JGXpISx5krkG+Eqh3wZ5Yg8txLFGof/NwF5V2jWEtMHesNDtv3gzObwlzorxF/UHHshxTAH2ZvEksyfw14pxfwkcXWdBPaliunbbnnorCul06dWFFbcryWxLSqxbAks1UlbFMDOB3QrlPljot3yO/e3AaqSjwpWqlHEq8L2KbvcBHwbeSUpA2wPDuollsXhJO0pPF9sFnE/hSLFi/E2BlfNytDNp47V1jWEnkTYYc0h7ngH8jDcT6reBCwrDL0XaIHfUaxMVyz6wJmnveWSh23HkI+s8/F8q1rNX6kyjIO3lzin8FTdaVxeG/Xhu25D8fWQef1QD6/i4POzQBtqwJ3BDYZ18mny0kKfzA4XxxudyxxS6PU9KXCIl9nUL/T5ATox52r9C3kblbs+QN8SVy0+VaXcU9RN4n9ZP2ul6tKKObwK/Lcyv6yv6Xw98F1il3rrS9VfW3WVjSXtqlX5M2tO6Kl/EPKKBsh7rQf9/krL3Kg1FWd/qubxi2UOBMYVuxbvBXiZl9UqrkPYQKssa24uYzgG+BmwD/KGi31rA+/MNGHMkzSElorcDSHq/pGmSnpX0ImmPqXI6NdKeeqrO94i4Fvg5ac9wtqTTJa1QqxBJn5c0s9COjSpiXRRnRLycP44gbWj+FREvVCl2LWByxfRZk7Sn/yBwMGmFekbSFEmrN9jm1YHHIuKNQrea8zcibo2I5yNiYURcDpwHfLJO+TdGxKhI12TeDrwH+GGh7kXLVY7hMWBsD9u0Omm6za3ThsplY9luzs9vmuPu+ruy0G924fMrwHPx5nWpV/L/4rLXyDreXRsuATaUtA7pyO/FiLi5TkxERGW3EaRrkMsDMwrL0Z9z9y7PR8TCwveerEvPk3aWaunr+tcCVq9YL45k8e1c5TZ4P9JR9L2SbpH0sXoN6vMkI2lz0oz9W2W/iJgbEZMjYh3SHsw3JG3X1btGkbW6d1mz8PkdpKON50jZfvlCXENYfEZ0V+6TpBlQLHshiy+MjXgux1RZ1hM9LAdSkvkKcHlh49rlMeC6ihV7RER03Y30O9Ih9poRsSLptKV6EUNVkkaQ9pr/Wq1/RPx3RGxG2kiuDxza1auinLVIp+2+RjqHPgq4s8FYHwNGSxpVo98PKqbP8hFxfo7vdxHxQdJ8CuCEGnVULjdPAmsW76ikZ/M3aHA+5I3e70nrTlfdi5YrSSKtD0/k4Wu1qVobRksa2cs2lK3WOl5Utw0R8SrputLewD6kdak3niMlnPcUlqMV805AI7rb7lwDrCFpQpPqf4x0FFRcL0ZGxM61xomIByLis8DbSMvU1Ho3/PRZkpG0Qs5oU0iH4rOqDPMxSe/MK8NLpMPbrj2Y2aTzgT31OUkbSlqedDpuat4rup+0t7WLpGGki+3LFMabDYyr2DgUnQ98XdLaeQP6Q9L1hoU1hq8qx3IB8ANJI/NG9BukC2k9EhEPk07vHFWl9x+B9SXtI2lY/ttc0rtz/5GkPb1XJW0B/L+e1l+NpGUkbUa6++UF0kX3ymE2z0dSw0jJ/1Vqz/fhpIX62TzuvqQjmW5FxFPAFcAvJK2Up8GHcu9fAV/KcUjS8LxsjJS0gaRtJS2TY3ulEF+lynhvym06LNfXQUoCU6qNLGkPSSMkLSVpB+BzpOTfrXx34SdIF94hLVe7SNouT9vJpFOzf++mTYst+xHxGOlGiOMkLSvpvaS91fMaiasJaq3jizTYhrNJp8Z2pRfrX67nDdKydJKktwFIGivpow0WUXc7FxEPkK4rna/084Wlc3v2knRECfXfDLwk6XBJy0kaImmjfLBQlaTPSVo1xzInd655h2RfJJnLJM0lZcSjgJ+SLqBVsx7wF9I52H8Av4iIztzvOOBb+ZDtkB7Ufw7pPOPTpAt+BwJExIukvf4zSHsz80kX0LtcmP8/L+nWKuX+Jpd9PenC5KvAAT2Iq+iAXP9DpCO83+Xyeywi/hYRT1bpPpd0gXIv0l7d06S9jK7E+hXg2DyvvkPaQC2Jw3JZ/yKtvDOArSJifpVhVyCtGC+QTmE8T7o7BtLt7hvm+X5xRNwNnEhaPmaTzo/f0IO49iHt6d5LOhd9MEBETCddVP55juNB0gYH0jQ6nrSX+DRpD+3IGuVXxruAtNHaKY//C+DzEXFvjfEPIi2Pc0inj79YWAeq+YDyb02Ae0jJ94DcpvtISepnue6Pk35SsKCbNlVb9j9LusbxJOlU7NERcXWduLpzuxb/nczJS1BW1XW8irptiIgbSNfsbo2IR5YgnsNJy8+Nkl4ibdM2aHDcxZafGsMcyJunl+eQ7rT8BOkCf5/Wn5P1x0nXmx4mLS9nkO6IrWVH4K68TJ5Cunb7aq2Buy4gmpn1O0o/Nj43Is7oo/KuBX7XV+VZ99r1B45mZovJp4A2BXZrdSyDiR+QaWZtT9JZpNNKB1fcgWYl8+kyMzMrjY9kzMysNAPimswqq6wS48aNa3UYDZk/fz7Dhw/OZ0QO5rbD4G7/YG479N/2z5gx47mIWLX7IcszIJLMuHHjmD59eqvDaEhnZycdHR2tDqMlBnPbYXC3fzC3Hfpv+yX9s/uhyuXTZWZmVhonGTMzK42TjJmZlcZJxszMSuMkY2ZmpXGSMTOz0jjJmJlZaZxkzMysNE4yZmZWmgHxi/+BaNwRf2pZ3Y8cv0vL6jYzK/KRjJmZlcZJxszMSuMkY2ZmpXGSMTOz0jjJmJlZaZxkzMysNE4yZmZWGicZMzMrjZOMmZmVxknGzMxK4yRjZmalcZIxM7PSlJpkJH1d0l2S7pR0vqRlJa0t6SZJD0j6X0lLlxmDmZm1TmlJRtJY4EBgQkRsBAwB9gJOAE6KiPWAF4D9yorBzMxaq+zTZUOB5SQNBZYHngK2Babm/mcBu5ccg5mZtYgiorzCpYOAHwCvAFcBBwE3RsQ7c/81gSvykU7luPsD+wOMGTNmsylTppQWZ1+aN28eI0aMYNYTL7YshvFjV2xJvV1tH6wGc/sHc9uh/7Z/m222mRERE1oZQ2kvLZO0ErAbsDYwB7gQ2KnKoFWzXEScDpwOMGHChOjo6Cgn0D7W2dlJR0cHk1r50rK9O1pSb1fbB6vB3P7B3HZw++sp83TZ9sDDEfFsRLwGXARsBYzKp88A1gCeLDEGMzNroTKTzKPAlpKWlyRgO+BuYBqwRx5mInBJiTGYmVkLlZZkIuIm0gX+W4FZua7TgcOBb0h6EFgZ+HVZMZiZWWuVdk0GICKOBo6u6PwQsEWZ9ZqZWf/gX/ybmVlpnGTMzKw0pZ4u6w/GNflW4snjF7b09mUzs/7ERzJmZlYaJxkzMyuNk4yZmZXGScbMzErjJGNmZqVxkjEzs9I4yZiZWWmcZMzMrDROMmZmVhonGTMzK42TjJmZlcZJxszMSuMkY2ZmpXGSMTOz0jjJmJlZaZxkzMysNE4yZmZWGicZMzMrjZOMmZmVxknGzMxK4yRjZmalcZIxM7PSOMmYmVlpnGTMzKw0TjJmZlYaJxkzMyuNk4yZmZXGScbMzErjJGNmZqVxkjEzs9J0m2QkfVrSyPz5W5IukrRp+aGZmdlA18iRzLcjYq6kDwIfBc4CTi03LDMzaweNJJnX8/9dgFMj4hJg6fJCMjOzdtFIknlC0i+BzwCXS1qmwfHMzGyQayRZfAa4EtgxIuYAo4FDS43KzMzaQrdJJiJeBp4BPpg7LQQeKDMoMzNrD43cXXY0cDjwzdxpGHBuI4VLGiVpqqR7Jd0j6QOSRku6WtID+f9KvQ/fzMz6s0ZOl30C2BWYDxARTwIjGyz/FODPEfEuYGPgHuAI4JqIWA+4Jn83M7M21EiSWRARAQSApOGNFCxpBeBDwK8BImJBvqazG+k2aPL/3XsatJmZDQxK+aPOANIhwHrAR4DjgP8EfhcRP+tmvE2A04G7SUcxM4CDgCciYlRhuBci4i2nzCTtD+wPMGbMmM2mTJnSg2a9adYTL/ZqvN4asxzMfqWpVb7F+LErtqTeefPmMWLEiJbU3R8M5vYP5rZD/23/NttsMyMiJrQyhm6TDICkjwA7AAKujIirGxhnAnAjsHVE3CTpFOAl4IBGkkzRhAkTYvr06d3GWc24I/7Uq/F6a/L4hZw4a2hT66z0yPG7tKTezs5OOjo6WlJ3fzCY2z+Y2w79t/2SWp5kGrnwPxy4NiIOBX4FLCdpWANlPw48HhE35e9TgU2B2ZJWy2WvRrpzzczM2lAj12SuB5aRNBb4C7AvcGZ3I0XE08BjkjbInbYjnTq7FJiYu00ELulhzGZmNkA0cl5HEfGypP2An0XEjyTd1mD5BwDnSVoaeIiUoJYCLsjlPQp8ujeBm5lZ/9dQkpH0AWBvYL8ejEdEzASqnQ/crrHwzMxsIGvkdNnBpB9i/iEi7pK0DjCt3LDMzKwddHtEEhHXAdcVvj8EHFhmUGZm1h66TTKSppF/iFkUEduWEpGZmbWNRq6tHFL4vCzwKdJDMs3MzOpq5HTZjIpON0i6rurAZmZmBY2cLhtd+LoUsBnw9tIiMjOzttHI6bIZpGsyIp0me5g3b2U2MzOrqZHTZWs3IxAzM2s/jZwuGwZ8mfTYfoBO4JcR8VqJcZmZWRto5HTZqaS3Yf4if98nd/tCWUGZmVl7aCTJbB4RGxe+Xyvp9rICMjOz9tHIY2Vel7Ru15f8WJnXywvJzMzaRSNHMocC0yQ9RLrDbC3S05TNzMzqauTusmskrQdsQEoy90bEv0uPzMzMBrxG3xO8GTAuD7+xJCLi7NKiMjOzttDILcznAOsCM3nzWkwATjJmZlZXI0cyE4ANI+ItT2I2MzOrp5G7y+7EzyozM7NeqHkkI+ky0mmxkcDdkm4GFl3wj4hdyw/PzMwGsnqny37StCjMzKwt1Uwy+bXLZmZmvdbINRkzM7NecZIxM7PS1Lvwf01EbCfphIg4vJlB2ZIZd8SfWlLvmTsOb0m9ZtZ/1bvwv5qkDwO7SppCeqTMIhFxa6mRmZnZgFcvyXwHOAJYA/hpRb8Ati0rKDMzaw/17i6bCkyV9O2I+F4TYzIzszbRyFOYvydpVwqvX46IP5YblpmZtYNu7y6TdBxwEHB3/jsodzMzM6urkQdk7gJsEhFvAEg6C7gN+GaZgZmZ2cDX6O9kRhU+r1hGIGZm1n4aOZI5DrhN0jTSbcwfwkcxZmbWgEYu/J8vqRPYnJRkDo+Ip8sOzMzMBr6GXr8cEU8Bl5Yci5mZtRk/u8zMzErjJGNmZqWpm2QkLSXpzmYFY2Zm7aVuksm/jbld0juaFI+ZmbWRRi78rwbcJelmYH5Xx4jYtZEKJA0BpgNPRMTHJK0NTAFGA7cC+0TEgh5HbmZm/V4jSea7S1jHQcA9wAr5+wnASRExRdJpwH7AqUtYh5mZ9UPdXviPiOuAR4Bh+fMtpCOQbklag/RYmjPyd5FeETA1D3IWsHuPozYzswGhkQdkfpGUFH6ZO40FLm6w/JOBw4A38veVgTkRsTB/fzyXZ2ZmbaiR02VfBbYAbgKIiAckva27kSR9DHgmImZI6ujqXGXQqDH+/sD+AGPGjKGzs7OBUN9q8viF3Q/Uh8Ys1/w6+4t58+b1ej61g8Hc/sHcdnD762kkyfw7IhakM10gaSg1EkOFrUmvbt4ZWJZ0TeZkYJSkofloZg3gyWojR8TpwOkAEyZMiI6OjgaqfKtJTX7f/eTxCzlxVkMPUmg7Z+44nN7Op3bQ2dk5aNs/mNsObn89jfwY8zpJRwLLSfoIcCFwWXcjRcQ3I2KNiBgH7AVcGxF7A9OAPfJgE4FLehW5mZn1e40kmSOAZ4FZwH8BlwPfWoI6Dwe+IelB0jWaXy9BWWZm1o818hTmN/KLym4inSa7LyIaOV1WLKMT6MyfHyJd4zEzszbXbZKRtAtwGvB/pAv3a0v6r4i4ouzgzMxsYGvkCvWJwDYR8SCApHWBPwFOMmZmVlcj12Se6Uow2UPAMyXFY2ZmbaTmkYykT+aPd0m6HLiAdE3m06Rf/ZuZmdVV73TZxwufZwMfzp+fBVYqLSIzM2sbNZNMROzbzEDMzKz9NHJ32drAAcC44vCNPurfzMwGr0buLruY9IPJy3jzQZdmZmbdaiTJvBoR/116JGZm1nYaSTKnSDoauAr4d1fHiGjonTJmzTCuyQ9C7fLI8bu0pF6zgaKRJDMe2If0srGu02WRv5uZmdXUSJL5BLBORCwoOxgb2GY98WLTX61gZv1bI7/4vx0YVXYgZmbWfho5khkD3CvpFha/JuNbmM3MrK5GkszRpUdhZmZtqZH3yVzXjEDMzKz9NPKL/7mku8kAlgaGAfMjYoUyAzMzs4GvkSOZkcXvknbHb7Y0M7MGNHJ32WIi4mL8GxkzM2tAI6fLPln4uhQwgTdPn5mZmdXUyN1lxffKLAQeAXYrJRozM2srjVyT8XtlzMysV+q9fvk7dcaLiPheCfGYmVkbqXckM79Kt+HAfsDKgJOMmZnVVe/1yyd2fZY0EjgI2BeYApxYazwzM7Muda/JSBoNfAPYGzgL2DQiXmhGYGZmNvDVuybzY+CTwOnA+IiY17SozMysLdT7MeZkYHXgW8CTkl7Kf3MlvdSc8MzMbCCrd02mx08DMBtsiq99njx+YVNf2uZXP9tA4ERiZmalcZIxM7PSOMmYmVlpnGTMzKw0TjJmZlYaJxkzMyuNk4yZmZXGScbMzErjJGNmZqVxkjEzs9KUlmQkrSlpmqR7JN0l6aDcfbSkqyU9kP+vVFYMZmbWWmUeySwEJkfEu4Etga9K2hA4ArgmItYDrsnfzcysDZWWZCLiqYi4NX+eC9wDjAV2I72bhvx/97JiMDOz1lJElF+JNA64HtgIeDQiRhX6vRARbzllJml/YH+AMWPGbDZlypRe1T3riRd7NV5vjVkOZr/S1Cr7jcHcdmh++8ePXbF5lXVj3rx5jBgxotVhtEx/bf8222wzIyImtDKG0pOMpBHAdcAPIuIiSXMaSTJFEyZMiOnTp/eq/nFNfPQ6pMe9nzir7gtH29Zgbjs0v/396VH/nZ2ddHR0tDqMlumv7ZfU8iRT6t1lkoYBvwfOi4iLcufZklbL/VcDnikzBjMza50y7y4T8Gvgnoj4aaHXpcDE/HkicElZMZiZWWuVeWy/NbAPMEvSzNztSOB44AJJ+wGPAp8uMQYzM2uh0pJMRPwNUI3e25VVr5mZ9R/+xb+ZmZXGScbMzErjJGNmZqVxkjEzs9I4yZiZWWmcZMzMrDSD9xkgZgNcsx+Z1KU/Pc7G+j8fyZiZWWmcZMzMrDROMmZmVhonGTMzK42TjJmZlcZJxszMSuMkY2ZmpXGSMTOz0jjJmJlZaZxkzMysNE4yZmZWGicZMzMrjZOMmZmVxknGzMxK4yRjZmalcZIxM7PS+KVlZtYj1V6WNnn8QiY14SVqfmHawOMjGTMzK42TjJmZlcZJxszMSuMkY2ZmpXGSMTOz0jjJmJlZaZxkzMysNE4yZmZWGv8Y08wGjGo/BG0G/wi093wkY2ZmpXGSMTOz0jjJmJlZaZxkzMysNE4yZmZWGicZMzMrTUtuYZa0I3AKMAQ4IyKOb0UcZmaN6O7W6bLep9MOt043/UhG0hDgf4CdgA2Bz0rasNlxmJlZ+VpxumwL4MGIeCgiFgBTgN1aEIeZmZVMEdHcCqU9gB0j4gv5+z7A+yPiaxXD7Q/sn79uANzX1EB7bxXguVYH0SKDue0wuNs/mNsO/bf9a0XEqq0MoBXXZFSl21syXUScDpxefjh9S9L0iJjQ6jhaYTC3HQZ3+wdz28Htr6cVp8seB9YsfF8DeLIFcZiZWclakWRuAdaTtLakpYG9gEtbEIeZmZWs6afLImKhpK8BV5JuYf5NRNzV7DhKNOBO8fWhwdx2GNztH8xtB7e/pqZf+Dczs8HDv/g3M7PSOMmYmVlpnGT6gKQ1JU2TdI+kuyQd1OqYWkHSEEm3Sfpjq2NpJkmjJE2VdG9eBj7Q6piaSdLX83J/p6TzJS3b6pjKJOk3kp6RdGeh22hJV0t6IP9fqZUx9idOMn1jITA5It4NbAl8dZA+Kucg4J5WB9ECpwB/joh3ARsziKaBpLHAgcCEiNiIdDPPXq2NqnRnAjtWdDsCuCYi1gOuyd8NJ5k+ERFPRcSt+fNc0kZmbGujai5JawC7AGe0OpZmkrQC8CHg1wARsSAi5rQ2qqYbCiwnaSiwPG3+u7eIuB74V0Xn3YCz8uezgN2bGlQ/5iTTxySNA94H3NTaSJruZOAw4I1WB9Jk6wDPAr/NpwrPkDS81UE1S0Q8AfwEeBR4CngxIq5qbVQtMSYinoK00wm8rcXx9BtOMn1I0gjg98DBEfFSq+NpFkkfA56JiBmtjqUFhgKbAqdGxPuA+QyiUyX52sNuwNrA6sBwSZ9rbVTWnzjJ9BFJw0gJ5ryIuKjV8TTZ1sCukh4hPVV7W0nntjakpnkceDwiuo5cp5KSzmCxPfBwRDwbEa8BFwFbtTimVpgtaTWA/P+ZFsfTbzjJ9AFJIp2TvyciftrqeJotIr4ZEWtExDjSRd9rI2JQ7M1GxNPAY5I2yJ22A+5uYUjN9iiwpaTl83qwHYPoxoeCS4GJ+fNE4JIWxtKvtOTNmG1oa2AfYJakmbnbkRFxeQtjsuY5ADgvP4vvIWDfFsfTNBFxk6SpwK2kuyxvo80fsSLpfKADWEXS48DRwPHABZL2IyXeT7cuwv7Fj5UxM7PS+HSZmZmVxknGzMxK4yRjZmalcZIxM7PSOMmYmVlpnGQGOEkh6ZzC96GSni37SciSzpT0sKTbJd0v6ez8sMSu/pdLGlVn/IMlLV9mjHXqniRp9R6O09Xemfnv730UyzGSDumLsvpKd9NH0iH5idN35vn/+V7Ws4mknXsfqQ0ETjID33xgI0nL5e8fAZ5oUt2HRsTGwAak30dMy78VISJ27uZBkQeTHqbYCpNIj0DpqUMjYpP8186/ap90YAYqAAAGQ0lEQVREjekj6UukZWyL/NTlDwHqZT2bAD1KMvkhnDaAOMm0hytIT0AG+CxwflcPScPz+y9uyQ9w3C13Hyfpr5JuzX9b5e4dkjoL70c5L/+Su6ZITgKeBnbK5TwiaZVc/5/yHu+dkvaUdCBpIzZN0rQ8/KmSpuf3kny3EP8jkr6bY5wl6V25+whJv83d7pD0qdx9B0n/yMNfmJ8nR6G8PYAJpB9PzpS0nKTt8rSZlafVMo1O+Hwkcpakq3Ksn5T0o1zWn/PjhrracYKkm/PfO6uUtYmkG3N7/iBpJUnrSrq1MMx6kmYUyvxhbu90SZtKulLS/+Vk0DXOoXn+39E1bfP8v0fSr/I0vypPi7dMn4owjwS+0vVsvoh4MSLOymVuJuk6STNyHF2PWekstP1+Sf+Rd0aOBfbM9exZZ1mdlOflZcBVklaTdH0e705J/9Ho/LIWiAj/DeA/YB7wXtIzs5YFZpJ+jfzH3P+HwOfy51HA/cBw0lHEsrn7esD0/LkDeBFYg7QT8g/gg1XqPRPYo6LbycDh+fMjwCrAp4BfFYZZsdi/0H10/j8E6ATeWxjugPz5K8AZ+fMJwMmF8VfK9V0PDM/dDge+UyX2TtL7T8jT7DFg/fz9bNIDTqu19+E8fWeSnlEHcAzwN2AY6V0yLwM75X5/AHYvtOOo/PnzhflzDHBI/nwH8OH8+diu9gHTgE0K8/OAQplfzp9PyuOPBFYlPbAUYAfSL/CV5+cfSUcf40i/0O8q9wLeXE4WTZ+KaTASeKHGcjgM+Duwav6+J/CbQnkn5s87A3/JnycBPy+UUWtZnUR6RlzXMjK5MC2HACNbvR76r/afDz3bQETcofSKgc8ClY+y2YH08Mqu8/7LAu8gvfPj55I2AV4H1i+Mc3NEPA6g9JiccaQNaXeqHfHMAn4i6QTShvWvNcb9jKT9SY86Wg3YkLTRhPTQRYAZwCfz5+0pvBwrIl5Qehr0hsAN+eBraVKSrGcD0gMe78/fzwK+SkqYlQ6NiKlVul8REa9JmkXa6P05d59FmnZdzi/8P6lYgKQVgVERcV0hjgvz5zOAfSV9g7Tx3qIw6qWFukZEep/RXEmvKl0T2yH/3ZaHG0HaqXg0t7vrMUgzKmKtRkCtR4RsAGwEXJ2n/RDSo/+7FOdhrXpqLasAV0dE1ztcbgF+k48SLy60wfohJ5n2cSnpvR4dwMqF7gI+FRH3FQeWdAwwm7T3vRTwaqH3vwufX6fx5eR9pLcCLhIR90vajLQHe5ykqyLi2IpY1gYOATbPyeJM0gamMp5iLNU2eCJtjD7bYLxd4yypfwNExBuSXou8i016t05x2kWNz935Pen5WNcCMyLi+cq6c13F+dZVt4DjIuKXxQLzTknlfK48NbaYiHhJ0nxJ60TEQxW9BdwVEbVePV1tHlaqtay+n3TtsSuO6yV9iHSK+BxJP46Is+vFbq3jazLt4zfAsRExq6L7lcAByruXkt6Xu68IPBURb5Ae7jmktxUrOZB0BPLnin6rAy9HxLmkJNj1GPy5pNMvACuQNiIvShpDvq7TjauArxXqWQm4Edi663qH0pOB168ybrHue4FxhWsk+wDXVRmnL+xZ+L/YEVZEvAi8ULi+sCiOiHiVNB9PBX7bwzqvBP6z69qUpLGSunuhVnH6VDoO+B+lN4IiaYV8BHofsKqkD+TuwyS9p4f11FpWFyNpLdLpwF+Rnn4+mF6tMOA4ybSJiHg8Ik6p0ut7pPPld0i6M38H+AUwUdKNpFNl86uM250fS7qddO58c2CbiFhQMcx44OZ82u0o4Pu5++nAFZKmRcTtpNM5d5GS5Q0N1P19YKV84ff2XPezpPP350u6g5R03lVl3DOB03JMIj01+cJ8uusN4LQ67Z1Z+Fu6gTiLlpF0E3AQ8PUq/SfmOu4g3XlVPOI7j3T006O3TkZ6S+XvgH/k9k2ldgLpciZ5+lS58H8q6RrRLXl5uo60E7EA2AM4Ic+PmXT/XplpwIZdF/6pvaxW6gBmSrqNdM2v2nJv/YSfwmzWBEovdJsQEc/1cvxDSDdNfLtPAzMrma/JmPVzkv4ArAts2+pYzHrKRzJmZlYaX5MxM7PSOMmYmVlpnGTMzKw0TjJmZlYaJxkzMyvN/wcNRLP/+mgtKAAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['dis'].hist()\n",
    "plt.title('Distribution of Mean Distances to 5 Boston Employment Centers')\n",
    "plt.xlabel('Mean Distance to Employment Centers')\n",
    "plt.ylabel('Number of houses')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can see from the above histogram that most houses in this sample are quite close to the employment centers of Boston. We have an obvious skewed distribution here."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'Number of Houses')"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['rm'].hist()\n",
    "plt.title('Distribution of Rooms per Household')\n",
    "plt.xlabel('Number of Rooms')\n",
    "plt.ylabel('Number of Houses')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The number of rooms in all houses are distributed normally and have a mean around 6. Either side of this, there are more larger homes than there smaller"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'Number of Houses')"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['medv'].hist()\n",
    "plt.title('Distribution of Median Home Values')\n",
    "plt.xlabel('Median Home Value')\n",
    "plt.ylabel('Number of Houses')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Most homes are valued at around 200k, which at this early stage we could deduce that many of them will be 6 room households. Whats striking here is that, one would normally assume all the values and room numbers would be extremely close to similar on the above graphs. Yet, it seems that there are many more houses below the average value than there are houses with below average room numbers."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x106d99fd0>"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['crim'].hist()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Above shows the crime rate per capita. Most of which are well below 10, lets see some quantiles for this data in comparison to the max value which confirms the above"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.26169000000000003"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['crim'].quantile(.5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "73.5341"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['crim'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9.958202"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['crim'].quantile(.9)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Boxplot to display the median home value "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1a19ea3ac8>"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['medv'].plot(kind='box')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can clearly see here our distribution of house values between around 5 and 35, leaving many outliers outside this range. This visualisation shows much clearer a link now with the 'number of rooms' histogram we looked at in the first instance. Looking at just the histograms first I was thrown off but this box plot seems to agree with the assumption that amount of rooms are equal to value of the house. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Investigating correlations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ID and rad have a correlation coefficient of 0.7075262711727565!\n",
      "indus and nox have a correlation coefficient of 0.7500874390908759!\n",
      "indus and tax have a correlation coefficient of 0.7083132697607584!\n",
      "nox and age have a correlation coefficient of 0.7359995828422857!\n",
      "rad and tax have a correlation coefficient of 0.9035618963206118!\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "for n, feat1 in enumerate(df.columns):\n",
    "    for feat2 in df.columns[n+1:]:\n",
    "        r2 = np.corrcoef(df[feat1], df[feat2])[0][1]\n",
    "        if r2 > .7:\n",
    "            print('{} and {} have a correlation coefficient of {}!'.format(feat1, feat2, r2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Average home values by home age')"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['decades'] = df.age // 10\n",
    "to_plot = df.groupby('decades').medv.mean()\n",
    "to_plot.plot(kind='barh', figsize=(10, 8))\n",
    "plt.ylabel('House age in decades')\n",
    "plt.xlabel('Average median value of homes')\n",
    "plt.title('Average home values by home age')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It is clear to see here that the approximate age of the house convincingly increases with its youth. Barring two slight variances at 20 and 50 years. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.6.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
