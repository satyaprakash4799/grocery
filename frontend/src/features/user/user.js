import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import apiCall from '../../api/axios';


const userAuthenticate = createAsyncThunk('user/authenticateUser', async(data)=> {
    const response = await apiCall('/api/token/','POST',data )
    return response.data;
})

const initialState = {
    user: {},
    token: {},
    status:'idle',
    error: null
}
export const userSlicer = createSlice({
    'name': 'user',
    initialState: initialState ,
    reducers: {
        getToken(state,action){
            state.token.accessToken = localStorage.getItem('accessToken');
            state.token.refreshToken = localStorage.getItem('refreshToken');
        }
    },
    extraReducers(builder) {
        builder
            .addCase(userAuthenticate.pending, (state) => {
                state.status = 'loading'
            })
            .addCase(userAuthenticate.fulfilled, (state,action) => {
                state.status = 'succeeded'
                state.token.accessToken = action.payload.access;
                state.token.refreshToken = action.payload.refresh;
                localStorage.setItem('accessToken', action.payload.access);
                localStorage.setItem('refreshToken', action.payload.refresh);
            })
            .addCase(userAuthenticate.rejected, (state, action) => {
                state.status = 'rejected';
            })
    }
});


export const { getToken } = userSlicer.actions;
export default userSlicer.reducer;
export {userAuthenticate};